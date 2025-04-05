"""
ASGI config for cv2 project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

# به جای تنظیم مستقیم ماژول تنظیمات، اجازه می‌دهیم فایل settings.py
# بر اساس متغیر محیطی DJANGO_ENV، فایل تنظیمات مناسب را انتخاب کند
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "cv2.settings")

application = get_asgi_application()
