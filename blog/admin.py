from django.contrib import admin
from .models import Post, Category, Tag, Comment
from django.utils.html import format_html
from django_summernote.admin import SummernoteModelAdmin
# Register your models here.


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    date_hierarchy = 'created_at'
    list_display = ('title', 'author', 'created_at', 'updated_at', 'status', 'login_required', 'category', 'is_login_required')
    list_filter = ('category', 'tags', 'status', 'login_required')
    search_fields = ('title', 'content')
    list_editable = ('category', 'status', 'login_required')
    list_per_page = 10
    empty_value_display = '-empty-'
    summernote_fields = ('content',)
    
    def is_login_required(self, obj):
        if obj.login_required:
            return format_html('<span style="color:red;"><i class="fas fa-lock"></i> بله</span>')
        return format_html('<span style="color:green;"><i class="fas fa-unlock"></i> خیر</span>')
    
    is_login_required.short_description = 'نیاز به لاگین'

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

