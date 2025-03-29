from django.contrib import admin
from .models import Post, Category, Tag, Comment


# Register your models here.


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_at'
    list_display = ('title', 'author', 'created_at', 'updated_at', 'status', 'category')
    list_filter = ('category', 'tags', 'status')
    search_fields = ('title', 'content')
    list_editable = ('category', 'status')
    list_per_page = 10
    empty_value_display = '-empty-'


