from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .models import Comment
from django.utils.text import slugify
from .models import Category
from taggit.models import Tag
from .forms import CommentForm
from django.contrib import messages

def blog(request):
    # دریافت دسته‌بندی و تگ از پارامتر URL
    category_name = request.GET.get('category')
    tag_name = request.GET.get('tag')
    
    # دریافت تمام پست‌های فعال
    all_posts = Post.objects.filter(status=True)
    
    # دریافت پست‌ها با فیلتر دسته‌بندی یا تگ
    posts = all_posts
    if category_name:
        posts = posts.filter(category__name=category_name)
    if tag_name:
        posts = posts.filter(tags__name=tag_name)
    posts = posts.order_by('-created_at')
    
    # دریافت تمام دسته‌بندی‌ها
    categories = Category.objects.all().distinct()
    
    # دریافت تمام تگ‌ها
    tags = Tag.objects.all()
    
    # اطمینان از اینکه همه پست‌ها slug دارند
    for post in posts:
        if not post.slug or post.slug == '':
            post.slug = slugify(post.title)
            # اگر متن فارسی است و slugify خالی برمی‌گرداند، از عنوان انگلیسی استفاده کنیم
            if not post.slug:
                post.slug = f"post-{post.id}"
            post.save()
            
    return render(request, 'blog/index.html', {
        'posts': posts,
        'all_posts_count': all_posts.count(),
        'categories': categories,
        'tags': tags,
        'selected_category': category_name,
        'selected_tag': tag_name
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
    context = {
        'post': post,
        'categories': categories,
        'reading_time': reading_time,
        'tags': post.tags.all(),
        'comments': comments,
        'form': form
    }
    
    return render(request, 'blog/blog-single.html', context)
