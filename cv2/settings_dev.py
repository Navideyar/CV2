"""
Django settings for cv2 project - Development Settings
"""

import os
from .settings_base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-_!%xuv8il!@!0zp)eso^)-b9&qjl!o_y29pnb#2x75#0ja6ry%"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['localhost', '127.0.0.1']

# Database settings for development
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# reCAPTCHA settings
RECAPTCHA_PUBLIC_KEY = "6LcFJzEnAAAAAI-8hoShDg728nMCH3kCXjv5Cjwa" 
RECAPTCHA_PRIVATE_KEY = "6LcFJzEnAAAAAJ4u--yT7zNZnz6x1PbVD8yvNE_j"
RECAPTCHA_REQUIRED_SCORE = 0.5
RECAPTCHA_DEFAULT_ACTION = "form"

# Email settings for development
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Disable security features in development
CSRF_COOKIE_SECURE = False
SESSION_COOKIE_SECURE = False
SECURE_SSL_REDIRECT = False 