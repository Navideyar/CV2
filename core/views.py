from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from blog.models import Post, Category

# Create your views here.
def index(request):
    # دریافت آخرین پست‌ها (فقط پست‌های فعال)
    latest_posts = Post.objects.filter(status=True).order_by('-created_at')[:4]
    
    # دریافت دسته‌بندی‌های هر پست
    for post in latest_posts:
        post.post_category = Category.objects.filter(post=post).first()
    
    context = {
        'latest_posts': latest_posts
    }
    
    return render(request, "index.html", context)

def about(request):
    return render(request, "about-me.html")

def contact(request):
    return render(request, "contact.html")


def policy(request):
    return render(request, 'policy-and-privacy.html')


def personal_website(request):
    return render(request, 'services/personal-website.html')

def corporate_website(request):
    return render(request, 'services/corporate-website.html')

def ecommerce_website(request):
    return render(request, 'services/ecommerce-website.html')

def testimonials(request):
    return render(request, 'services/testimonials.html')





