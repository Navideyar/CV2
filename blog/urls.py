from django.urls import path
from . import views
from blog.feeds import LatestPostsFeed

app_name = 'blog'

urlpatterns = [
     path('', views.blog, name='blog'),
     path('<slug:slug>/', views.blog_single, name='blog_single'),
     path('rss/feed/' , LatestPostsFeed(), name='rss_feed')
]
