"""
تنظیمات محیط تولید (Production) برای پروژه cv2
"""

import os
import dj_database_url
from cv2.setting.base import *

# تنظیمات امنیتی
DEBUG = True  # موقتاً فعال می‌کنیم تا خطا را ببینیم
SECRET_KEY = os.environ.get("SECRET_KEY")
# پذیرش همه دامنه‌ها و آدرس‌های IP
ALLOWED_HOSTS = ['*']

# تنظیمات proxy - برای کار با nginx
USE_X_FORWARDED_HOST = True
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# تنظیمات دیتابیس
DATABASE_URL = os.environ.get('DATABASE_URL')
if DATABASE_URL:
    DATABASES = {'default': dj_database_url.config(default=DATABASE_URL)}
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': os.environ.get('DB_NAME', 'postgres'),
            'USER': os.environ.get('DB_USER', 'root'),
            'PASSWORD': os.environ.get('DB_PASSWORD', ''),
            'HOST': os.environ.get('DB_HOST', 'navidyar-database'),
            'PORT': os.environ.get('DB_PORT', '5432'),
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

# تنظیمات امنیتی HTTPS - موقتاً غیرفعال می‌کنیم
CSRF_COOKIE_SECURE = False
SESSION_COOKIE_SECURE = False
SECURE_BROWSER_XSS_FILTER = False
SECURE_CONTENT_TYPE_NOSNIFF = False
SECURE_HSTS_SECONDS = 0
SECURE_HSTS_INCLUDE_SUBDOMAINS = False
SECURE_HSTS_PRELOAD = False
SECURE_SSL_REDIRECT = False

# تنظیمات فشرده‌سازی
COMPRESS_OFFLINE = True 