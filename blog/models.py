from django.db import models
from django.contrib.auth.models import User
from taggit.managers import TaggableManager
from django.utils.text import slugify

class Category(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name
        
    def get_post_count(self):
        return self.post_set.filter(status=True).count()


class Tag(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    
class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    title = models.CharField(max_length=200 , unique=True )
    slug = models.SlugField(max_length=255, unique=True, null=True, blank=True)
    content = models.TextField()
    image = models.ImageField(upload_to='blog_images/', default='blog_images/default.jpg')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    tags = TaggableManager()
    count_views = models.IntegerField(default=0)
    status = models.BooleanField(default=False)
    publish_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    login_required = models.BooleanField(default=False)
    
    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    email = models.EmailField(blank=True, null=True)
    subject = models.CharField(max_length=200, blank=True, null=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    approved = models.BooleanField(default=False)
    
    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.name
