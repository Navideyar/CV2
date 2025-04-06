#!/usr/bin/env python
"""
اسکریپت بررسی وضعیت دیتابیس
این اسکریپت اتصال به دیتابیس را بررسی می‌کند و برخی اطلاعات اولیه را نمایش می‌دهد.
"""

import os
import sys
import django
from pathlib import Path

# تنظیم مسیر پروژه
BASE_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(BASE_DIR))

# تنظیم متغیرهای محیطی
os.environ.setdefault("DJANGO_ENVIRONMENT", "production")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "cv2.setting.production")

# بارگذاری تنظیمات محیطی
try:
    from load_env import load_env_file
    env_file_path = os.path.join(BASE_DIR, '.env.production')
    if os.path.exists(env_file_path):
        load_env_file(env_file_path)
        print(f"Loaded environment variables from {env_file_path}")
    else:
        print(f"Warning: {env_file_path} not found")
except Exception as e:
    print(f"Error loading environment variables: {e}")

# راه‌اندازی جنگو
try:
    django.setup()
    print("Django setup completed successfully")
except Exception as e:
    print(f"Error setting up Django: {e}")
    sys.exit(1)

# وارد کردن مدل‌ها
try:
    from blog.models import Post, Category, Tag as BlogTag
    from taggit.models import Tag as TaggitTag
    from django.contrib.auth.models import User
    from django.db import connection
except Exception as e:
    print(f"Error importing models: {e}")
    sys.exit(1)

def check_database_connection():
    """بررسی اتصال به دیتابیس"""
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT version();")
            version = cursor.fetchone()
        print(f"Database connection successful. Database version: {version[0]}")
        return True
    except Exception as e:
        print(f"Error connecting to database: {e}")
        return False

def check_models_data():
    """بررسی داده‌های موجود در مدل‌ها"""
    try:
        # بررسی کاربران
        user_count = User.objects.count()
        print(f"User count: {user_count}")
        if user_count > 0:
            print(f"Sample users: {', '.join([user.username for user in User.objects.all()[:5]])}")
        
        # بررسی پست‌ها
        post_count = Post.objects.count()
        print(f"Post count: {post_count}")
        if post_count > 0:
            posts = Post.objects.all()[:5]
            print(f"Sample posts: {', '.join([post.title for post in posts])}")
            
            # بررسی عمیق‌تر یک پست نمونه برای بررسی تگ‌ها
            if posts:
                sample_post = posts[0]
                print(f"\nDetailed check of post: {sample_post.title}")
                print(f"Post ID: {sample_post.id}")
                print(f"Post slug: {sample_post.slug}")
                print(f"Post status: {sample_post.status}")
                print(f"Post tags: {', '.join([tag.name for tag in sample_post.tags.all()])}")
                
                if hasattr(sample_post, 'category') and sample_post.category:
                    print(f"Post category: {sample_post.category.name}")
                else:
                    print("Post has no category")
        
        # بررسی دسته‌بندی‌ها
        category_count = Category.objects.count()
        print(f"Category count: {category_count}")
        if category_count > 0:
            print(f"Sample categories: {', '.join([cat.name for cat in Category.objects.all()[:5]])}")
        
        # بررسی تگ‌های Blog
        blog_tag_count = BlogTag.objects.count()
        print(f"Blog Tag count: {blog_tag_count}")
        if blog_tag_count > 0:
            print(f"Sample blog tags: {', '.join([tag.name for tag in BlogTag.objects.all()[:5]])}")
        
        # بررسی تگ‌های Taggit
        taggit_tag_count = TaggitTag.objects.count()
        print(f"Taggit Tag count: {taggit_tag_count}")
        if taggit_tag_count > 0:
            print(f"Sample taggit tags: {', '.join([tag.name for tag in TaggitTag.objects.all()[:5]])}")
        
        return True
    except Exception as e:
        print(f"Error checking model data: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    print("=" * 50)
    print("DATABASE STATUS CHECK")
    print("=" * 50)
    
    # نمایش اطلاعات متغیرهای محیطی دیتابیس
    print("\nDatabase Environment Variables:")
    print(f"DATABASE_URL: {os.environ.get('DATABASE_URL', 'Not Set')}")
    print(f"DB_NAME: {os.environ.get('DB_NAME', 'Not Set')}")
    print(f"DB_USER: {os.environ.get('DB_USER', 'Not Set')}")
    print(f"DB_HOST: {os.environ.get('DB_HOST', 'Not Set')}")
    print(f"DB_PORT: {os.environ.get('DB_PORT', 'Not Set')}")
    
    # بررسی اتصال به دیتابیس
    print("\nChecking database connection:")
    if check_database_connection():
        # بررسی داده‌های مدل‌ها
        print("\nChecking model data:")
        check_models_data()
    
    print("\nDatabase check completed.")
    print("=" * 50) 