"""
Django settings for cv2 project.

This file is used to determine which settings to load based on the environment.
"""

import os

# تعیین محیط بر اساس متغیر محیطی DJANGO_ENV
# اگر متغیر محیطی تعریف نشده باشد، به طور پیش‌فرض از محیط توسعه استفاده می‌شود
DJANGO_ENV = os.environ.get('DJANGO_ENV', 'development')

if DJANGO_ENV == 'production':
    from .production_settings import *
else:
    from .settings_dev import *
