from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
     path('', views.blog, name='blog'),
     path('<int:id>/', views.blog_single, name='blog_single'),
]
