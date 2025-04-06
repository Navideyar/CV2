"""
DEPRECATED - این فایل دیگر استفاده نمی‌شود.
لطفا از فایل‌های جدید در پوشه cv2/setting استفاده کنید.

<<<<<<< HEAD
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
=======
این فایل فقط به عنوان مرجع نگهداری شده است.
"""

# All settings moved to cv2/setting/base.py, cv2/setting/development.py and cv2/setting/production.py
>>>>>>> test
