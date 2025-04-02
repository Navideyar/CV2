from django.contrib import admin
from .models import Post, Category, Tag, Comment
from django.utils.html import format_html
from django_summernote.admin import SummernoteModelAdmin
# Register your models here.


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    date_hierarchy = 'created_at'
    list_display = ('title', 'author', 'created_at', 'updated_at', 'status', 'category')
    list_filter = ('category', 'tags', 'status')
    search_fields = ('title', 'content')
    list_editable = ('category', 'status')
    list_per_page = 10
    empty_value_display = '-empty-'
    summernote_fields = ('content',)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'short_message', 'post', 'created_at', 'approved')
    list_filter = ('post', 'created_at', 'approved')
    search_fields = ('name', 'post__title', 'message')
    list_editable = ('approved',)
    list_per_page = 10
    empty_value_display = '-empty-'
    
    def short_message(self, obj):
        return obj.message[:35] + '...' if len(obj.message) > 35 else obj.message
    
    short_message.short_description = 'Message'

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_per_page = 10
    empty_value_display = '-empty-'

