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

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'post', 'created_at')
    list_filter = ('post', 'created_at')
    search_fields = ('user__username', 'post__title')
    list_per_page = 10
    empty_value_display = '-empty-'

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_per_page = 10
    empty_value_display = '-empty-'
