"""
تنظیمات محیط تولید (Production) برای پروژه cv2
"""

import os
import dj_database_url
from cv2.setting.base import *

# تنظیمات امنیتی
DEBUG = False  # در محیط پروداکشن باید غیرفعال باشد
SECRET_KEY = os.environ.get("SECRET_KEY")
# پذیرش همه دامنه‌ها و آدرس‌های IP
ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', '*').split(', ')

# تنظیمات proxy - برای کار با nginx
USE_X_FORWARDED_HOST = True
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# تنظیمات دیتابیس با بهبود خطایابی
DATABASE_URL = os.environ.get('DATABASE_URL')
print(f"DEBUG - DATABASE_URL: {DATABASE_URL}", flush=True)

if DATABASE_URL:
    print("Using DATABASE_URL for database configuration", flush=True)
    # اصلاح URL برای پشتیبانی از هر دو فرمت postgresql:// و postgres://
    if DATABASE_URL.startswith('postgresql://'):
        print("Using postgresql:// protocol", flush=True)
        db_config = dj_database_url.config(default=DATABASE_URL)
    elif DATABASE_URL.startswith('postgres://'):
        print("Using postgres:// protocol", flush=True)
        db_config = dj_database_url.config(default=DATABASE_URL)
    else:
        print(f"Unknown database URL format: {DATABASE_URL}", flush=True)
        # تلاش برای استفاده از هر فرمتی
        db_config = dj_database_url.config(default=DATABASE_URL)
    
    DATABASES = {'default': db_config}
    print(f"Database config: ENGINE={db_config.get('ENGINE', 'unknown')}, NAME={db_config.get('NAME', 'unknown')}, HOST={db_config.get('HOST', 'unknown')}", flush=True)
else:
    print("Using individual database settings", flush=True)
    DB_NAME = os.environ.get('DB_NAME', 'postgres')
    DB_USER = os.environ.get('DB_USER', 'root')
    DB_PASSWORD = os.environ.get('DB_PASSWORD', '')
    DB_HOST = os.environ.get('DB_HOST', 'navidyar-database')
    DB_PORT = os.environ.get('DB_PORT', '5432')
    
    print(f"DEBUG - DB_NAME: {DB_NAME}", flush=True)
    print(f"DEBUG - DB_USER: {DB_USER}", flush=True)
    print(f"DEBUG - DB_HOST: {DB_HOST}", flush=True)
    print(f"DEBUG - DB_PORT: {DB_PORT}", flush=True)
    
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': DB_NAME,
            'USER': DB_USER,
            'PASSWORD': DB_PASSWORD,
            'HOST': DB_HOST,
            'PORT': DB_PORT,
            'OPTIONS': {
                'client_encoding': 'UTF8',
            },
        }
    }

# تنظیمات ایمیل
EMAIL_BACKEND = os.environ.get('EMAIL_BACKEND', 'django.core.mail.backends.smtp.EmailBackend')
EMAIL_HOST = os.environ.get('EMAIL_HOST', '')
EMAIL_PORT = int(os.environ.get('EMAIL_PORT', 587))
EMAIL_USE_TLS = os.environ.get('EMAIL_USE_TLS', 'True') == 'True'
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER', '')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD', '')
DEFAULT_FROM_EMAIL = os.environ.get('DEFAULT_FROM_EMAIL', '')

# تنظیمات reCAPTCHA
RECAPTCHA_PUBLIC_KEY = os.environ.get("RECAPTCHA_PUBLIC_KEY", "")
RECAPTCHA_PRIVATE_KEY = os.environ.get("RECAPTCHA_PRIVATE_KEY", "")
RECAPTCHA_REQUIRED_SCORE = 0.5
RECAPTCHA_DEFAULT_ACTION = "form"

# تنظیمات امنیتی HTTPS
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_HSTS_SECONDS = 31536000  # یک سال
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True
SECURE_SSL_REDIRECT = True

# تنظیمات فشرده‌سازی
COMPRESS_OFFLINE = True 