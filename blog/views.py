from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Post
from .models import Comment
from django.utils.text import slugify

def blog(request):
    posts = Post.objects.filter(status=True).order_by('-created_at')
    
    # اطمینان از اینکه همه پست‌ها slug دارند
    for post in posts:
        if not post.slug or post.slug == '':
            post.slug = slugify(post.title)
            # اگر متن فارسی است و slugify خالی برمی‌گرداند، از عنوان انگلیسی استفاده کنیم
            if not post.slug:
                post.slug = f"post-{post.id}"
            post.save()
            
    return render(request, 'blog/index.html', {'posts': posts})

def blog_single(request, slug):
    # اگر slug خالی باشد، به صفحه اصلی وبلاگ برگردیم
    if not slug or slug == '':
        return redirect('blog:blog')
        
    post = get_object_or_404(Post, slug=slug , status=True  )
    return render(request, 'blog/blog-single.html', {'post': post})
