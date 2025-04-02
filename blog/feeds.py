from django.contrib.syndication.views import Feed
from django.urls import reverse
from django.utils.html import strip_tags
from django.utils.text import Truncator
from .models import Post

class LatestPostsFeed(Feed):
    title = "My Blog"
    link = "/blog/"
    description = "New posts of my blog"

    def items(self):
        return Post.objects.filter(status=True)
    
    def item_title(self, item):
        return item.title
    
    def item_description(self, item):
        return Truncator(strip_tags(item.content)).words(30)
        
    def item_link(self, item):
        return reverse('blog:blog_single', args=[item.slug])