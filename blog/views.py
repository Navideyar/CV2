from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from .models import Comment

def blog(request):
    posts = Post.objects.filter(status=True).order_by('-created_at')
    return render(request, 'blog/index.html', {'posts': posts})

def blog_single(request, id):
    post = Post.objects.get(id=id)
    return render(request, 'blog/blog-single.html', {'post': post})
