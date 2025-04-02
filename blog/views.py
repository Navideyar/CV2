from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .models import Comment
from django.utils.text import slugify
from .models import Category
from taggit.models import Tag
from .forms import CommentForm
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def blog(request):
    # دریافت دسته‌بندی و تگ از پارامتر URL
    category_name = request.GET.get('category')
    tag_name = request.GET.get('tag')
    search_query = request.GET.get('q')
    sort_type = request.GET.get('sort', 'newest')  # مقدار پیش‌فرض: جدیدترین
    
    # دریافت تمام پست‌های فعال
    all_posts = Post.objects.filter(status=True)
    
    # دریافت پست‌ها با فیلتر دسته‌بندی یا تگ یا جستجو
    posts = all_posts
    if category_name:
        posts = posts.filter(category__name=category_name)
    if tag_name:
        posts = posts.filter(tags__name=tag_name)
    if search_query:
        posts = posts.filter(title__icontains=search_query) | posts.filter(content__icontains=search_query)
    
    # مرتب‌سازی پست‌ها بر اساس پارامتر sort
    if sort_type == 'newest':
        posts = posts.order_by('-created_at')
    elif sort_type == 'oldest':
        posts = posts.order_by('created_at')
    elif sort_type == 'popular':
        posts = posts.order_by('-count_views')
    else:
        posts = posts.order_by('-created_at')  # مرتب‌سازی پیش‌فرض
    
    # دریافت تمام دسته‌بندی‌ها
    categories = Category.objects.all().distinct()
    
    # دریافت تمام تگ‌ها
    tags = Tag.objects.all()
    
    # دریافت آخرین پست‌ها برای نمایش در سایدبار
    latest_posts = Post.objects.filter(status=True).order_by('-created_at')[:3]
    
    # اطمینان از اینکه همه پست‌ها slug دارند
    for post in posts:
        if not post.slug or post.slug == '':
            post.slug = slugify(post.title)
            # اگر متن فارسی است و slugify خالی برمی‌گرداند، از عنوان انگلیسی استفاده کنیم
            if not post.slug:
                post.slug = f"post-{post.id}"
            post.save()
    
    # صفحه‌بندی
    page = request.GET.get('page', 1)
    posts_per_page = 5  # تعداد پست در هر صفحه
    paginator = Paginator(posts, posts_per_page)
    
    try:
        paginated_posts = paginator.page(page)
    except PageNotAnInteger:
        # اگر شماره صفحه عدد نباشد، صفحه اول نمایش داده شود
        paginated_posts = paginator.page(1)
    except EmptyPage:
        # اگر شماره صفحه بیشتر از تعداد صفحات باشد، آخرین صفحه نمایش داده شود
        paginated_posts = paginator.page(paginator.num_pages)
            
    return render(request, 'blog/index.html', {
        'posts': paginated_posts,
        'all_posts_count': posts.count(),  # تعداد پست‌های فیلتر شده
        'total_posts_count': all_posts.count(),  # تعداد کل پست‌ها
        'categories': categories,
        'tags': tags,
        'selected_category': category_name,
        'selected_tag': tag_name,
        'search_query': search_query,
        'sort_type': sort_type,
        'latest_posts': latest_posts
    })


def blog_single(request, slug):
    # اگر slug خالی باشد، به صفحه اصلی وبلاگ برگردیم
    if not slug or slug == '':
        return redirect('blog:blog')
        
    post = get_object_or_404(Post, slug=slug, status=True)
    
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            messages.success(request, 'نظر شما با موفقیت ثبت شد و پس از تایید نمایش داده خواهد شد')
            return redirect('blog:blog_single', slug=slug)
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"خطا در فیلد {field}: {error}")
    else:
        form = CommentForm()
        
    comments = Comment.objects.filter(post=post.id, approved=True).order_by('-created_at')
    
    # دریافت دسته‌بندی‌های مرتبط با پست
    categories = Category.objects.filter(post=post)  
    
    # افزایش تعداد بازدید
    post.count_views += 1
    post.save()

    # محاسبه زمان مطالعه تقریبی (هر 200 کلمه حدود یک دقیقه)
    word_count = len(post.content.split())
    reading_time = max(1, round(word_count / 200))
    
    # دریافت آخرین پست‌ها برای نمایش در سایدبار
    latest_posts = Post.objects.filter(status=True).exclude(id=post.id).order_by('-created_at')[:3]
    
    context = {
        'post': post,
        'categories': categories,
        'reading_time': reading_time,
        'tags': post.tags.all(),
        'comments': comments,
        'form': form,
        'latest_posts': latest_posts
    }
    
    return render(request, 'blog/blog-single.html', context)
