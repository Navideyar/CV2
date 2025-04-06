"""
تنظیمات پایه جنگو برای پروژه cv2

این فایل شامل تنظیمات مشترک بین محیط‌های توسعه و تولید است.
"""

from pathlib import Path
import os

# مسیر پایه پروژه
BASE_DIR = Path(__file__).resolve().parent.parent.parent

# برنامه‌های نصب شده
INSTALLED_APPS = [
    'multi_captcha_admin',
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.sites",
    "django.contrib.sitemaps",
    "django_summernote",
    "compressor",
    "blog",
    "contact",
    'accounts',
    'core',
    'taggit',
    'robots',
    'django_recaptcha',
    'captcha',
    'django.contrib.humanize',
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "cv2.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "cv2.wsgi.application"

# تنظیمات اعتبارسنجی رمز عبور
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

# تنظیمات بین‌المللی‌سازی
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

# تنظیمات فایل‌های استاتیک
STATIC_URL = "static/" 
STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")

# تنظیمات فایل‌های رسانه‌ای
MEDIA_URL = "media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

# تنظیمات کلید اصلی پیش‌فرض
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# تنظیمات چندرسانه‌ای
X_FRAME_OPTIONS = 'SAMEORIGIN'
SUMMERNOTE_THEME = 'bs4'
SUMMERNOTE_CONFIG = {
    'iframe': True,
    'summernote': {
        'height': '400px',
        'toolbar': [
            ['style', ['style']],
            ['font', ['bold', 'underline', 'clear']],
            ['fontname', ['fontname']],
            ['color', ['color']],
            ['para', ['ul', 'ol', 'paragraph']],
        ],
    },
}

# تنظیمات Compressor
STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
]

COMPRESS_ENABLED = True
COMPRESS_CSS_HASHING_METHOD = None

# تنظیمات کپچا
MULTI_CAPTCHA_ADMIN = {
    "ENGINE": "simple-captcha",
}

# تنظیمات نقشه سایت
SITE_ID = 1

# تنظیمات robots.txt
robots_use_https = True
robots_use_sitemap = True 