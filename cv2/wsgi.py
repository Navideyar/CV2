"""
WSGI config for cv2 project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

<<<<<<< HEAD
# به جای تنظیم مستقیم ماژول تنظیمات، اجازه می‌دهیم فایل settings.py
# بر اساس متغیر محیطی DJANGO_ENV، فایل تنظیمات مناسب را انتخاب کند
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "cv2.settings")
=======
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "cv2.setting")
>>>>>>> test

application = get_wsgi_application()
