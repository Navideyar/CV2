"""
WSGI config for cv2 project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

import os
import sys

print("wsgi.py is being executed!", flush=True)
print(f"Python version: {sys.version}", flush=True)
print(f"Current working directory: {os.getcwd()}", flush=True)

from django.core.wsgi import get_wsgi_application

# اصلاح مسیر ماژول تنظیمات برای استفاده مستقیم از فایل تنظیمات تولید
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "cv2.setting.production")

print(f"DJANGO_SETTINGS_MODULE: {os.environ.get('DJANGO_SETTINGS_MODULE')}", flush=True)
print(f"DJANGO_ENVIRONMENT: {os.environ.get('DJANGO_ENVIRONMENT')}", flush=True)

application = get_wsgi_application()

print("wsgi.py execution completed - application initialized", flush=True)
