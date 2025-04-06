"""
WSGI config for cv2 project.

این فایل wsgi در ریشه پروژه قرار دارد و برای لیارا ساده‌تر خواهد بود تا آن را پیدا کند.
"""

import os

# تنظیم متغیر محیطی DJANGO_ENVIRONMENT به production
os.environ["DJANGO_ENVIRONMENT"] = "production"

# تنظیم مسیر ماژول تنظیمات
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "cv2.setting")

# افزودن مسیر فعلی به مسیرهای پایتون برای اطمینان از وارد شدن ماژول‌ها
import sys
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent
if str(BASE_DIR) not in sys.path:
    sys.path.insert(0, str(BASE_DIR))

# چاپ تنظیمات و مسیرها برای کمک به تشخیص مشکلات
print(f"Python version: {sys.version}", flush=True)
print(f"Python executable: {sys.executable}", flush=True)
print(f"Working directory: {os.getcwd()}", flush=True)
print(f"BASE_DIR: {BASE_DIR}", flush=True)
print(f"sys.path: {sys.path}", flush=True)
print(f"DJANGO_SETTINGS_MODULE: {os.environ.get('DJANGO_SETTINGS_MODULE')}", flush=True)
print(f"DJANGO_ENVIRONMENT: {os.environ.get('DJANGO_ENVIRONMENT')}", flush=True)

try:
    # وارد کردن تابع کاربردی جنگو
    from django.core.wsgi import get_wsgi_application
    
    # ساخت و بازگرداندن اپلیکیشن WSGI
    application = get_wsgi_application()
    print("Django WSGI application loaded successfully", flush=True)
except Exception as e:
    print(f"Error loading Django WSGI application: {e}", flush=True)
    
    # حتی اگر جنگو بارگذاری نشد، یک تابع ساده WSGI برای تست ارائه می‌دهیم
    def application(environ, start_response):
        status = '200 OK'
        output = f'Django WSGI application failed to load: {e}'.encode('utf-8')
        response_headers = [('Content-type', 'text/plain; charset=utf-8'),
                            ('Content-Length', str(len(output)))]
        start_response(status, response_headers)
        return [output] 