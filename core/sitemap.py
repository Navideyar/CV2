from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from blog.models import Post
from django.utils import timezone

class BlogSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.9

    def items(self):
        return Post.objects.filter(status=True, publish_at__lte=timezone.now())

    def lastmod(self, obj):
        return obj.updated_at

    def location(self, obj):
        return f'/blog/{obj.slug}/'

class StaticSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.8

    def items(self):
        return ['main_core:index', 'main_core:about', 'main_core:policy', 'main_core:personal_website', 
                'main_core:corporate_website', 'main_core:ecommerce_website', 'main_core:testimonials']

    def location(self, item):
        return reverse(item) 