from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Post
from .models import Comment
from django.utils.text import slugify
from .models import Category

def blog(request):
    # دریافت دسته‌بندی از پارامتر URL
    category_name = request.GET.get('category')
    
    # دریافت تمام پست‌های فعال
    all_posts = Post.objects.filter(status=True)
    
    # دریافت پست‌ها با فیلتر دسته‌بندی
    posts = all_posts
    if category_name:
        posts = posts.filter(category__name=category_name)
    posts = posts.order_by('-created_at')
    
    # دریافت تمام دسته‌بندی‌ها
    categories = Category.objects.all().distinct()
    
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
        'selected_category': category_name
    })

def blog_single(request, slug):
    # اگر slug خالی باشد، به صفحه اصلی وبلاگ برگردیم
    if not slug or slug == '':
        return redirect('blog:blog')
        
    post = get_object_or_404(Post, slug=slug, status=True)
    
    # دریافت دسته‌بندی‌های مرتبط با پست
    # به احتمال زیاد فیلد category به صورت ManyToMany تعریف شده است
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
        'reading_time': reading_time
    }
    return render(request, 'blog/blog-single.html', context)
