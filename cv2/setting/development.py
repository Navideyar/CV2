"""
تنظیمات محیط توسعه (Development) برای پروژه cv2
"""

import os
from .base import *

# تنظیمات امنیتی
DEBUG = True
SECRET_KEY = os.environ.get("SECRET_KEY", "django-insecure-_!%xuv8il!@!0zp)eso^)-b9&qjl!o_y29pnb#2x75#0ja6ry%")
ALLOWED_HOSTS = ['localhost', '127.0.0.1']

# تنظیمات دیتابیس
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# تنظیمات ایمیل
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
EMAIL_HOST = ''
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
DEFAULT_FROM_EMAIL = 'development@example.com'

# تنظیمات reCAPTCHA
RECAPTCHA_PUBLIC_KEY = os.environ.get("RECAPTCHA_PUBLIC_KEY", "6LcFJzEnAAAAAI-8hoShDg728nMCH3kCXjv5Cjwa")
RECAPTCHA_PRIVATE_KEY = os.environ.get("RECAPTCHA_PRIVATE_KEY", "6LcFJzEnAAAAAJ4u--yT7zNZnz6x1PbVD8yvNE_j")
RECAPTCHA_REQUIRED_SCORE = 0.5
RECAPTCHA_DEFAULT_ACTION = "form"

# فعال کردن ابزارهای توسعه (مانند Django Debug Toolbar)
try:
    import debug_toolbar
    INSTALLED_APPS += ['debug_toolbar']
    MIDDLEWARE += ['debug_toolbar.middleware.DebugToolbarMiddleware']
    INTERNAL_IPS = ['127.0.0.1']
except ImportError:
    pass 