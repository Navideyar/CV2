"""
WSGI config for cv2 project.

این فایل wsgi در ریشه پروژه قرار دارد و برای لیارا ساده‌تر خواهد بود تا آن را پیدا کند.
"""

import os
import sys
from pathlib import Path

# افزودن مسیر فعلی به مسیرهای پایتون برای اطمینان از وارد شدن ماژول‌ها
BASE_DIR = Path(__file__).resolve().parent
if str(BASE_DIR) not in sys.path:
    sys.path.insert(0, str(BASE_DIR))

# بارگذاری فایل محیطی
from load_env import load_env_file
env_file_path = os.path.join(BASE_DIR, '.env.production')
if os.path.exists(env_file_path):
    load_env_file(env_file_path)
    print(f"Loaded environment variables from {env_file_path}", flush=True)
else:
    print(f"Warning: {env_file_path} not found, falling back to environment variables", flush=True)

# تنظیم متغیر محیطی DJANGO_ENVIRONMENT به production
os.environ["DJANGO_ENVIRONMENT"] = "production"

# تنظیم مسیر ماژول تنظیمات
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "cv2.setting.production")

# تنظیم ALLOWED_HOSTS به صورت صریح
if "ALLOWED_HOSTS" not in os.environ:
    os.environ["ALLOWED_HOSTS"] = "*"

# چاپ تنظیمات و مسیرها برای کمک به تشخیص مشکلات
print("=================== STARTING WSGI APPLICATION ===================", flush=True)
print(f"Python version: {sys.version}", flush=True)
print(f"Python executable: {sys.executable}", flush=True)
print(f"Working directory: {os.getcwd()}", flush=True)
print(f"BASE_DIR: {BASE_DIR}", flush=True)
print(f"sys.path: {sys.path}", flush=True)
print(f"DJANGO_SETTINGS_MODULE: {os.environ.get('DJANGO_SETTINGS_MODULE')}", flush=True)
print(f"DJANGO_ENVIRONMENT: {os.environ.get('DJANGO_ENVIRONMENT')}", flush=True)
print(f"ALLOWED_HOSTS: {os.environ.get('ALLOWED_HOSTS')}", flush=True)
print(f"DATABASE_URL: {os.environ.get('DATABASE_URL', 'Not Set')}", flush=True)
print(f"DB_NAME: {os.environ.get('DB_NAME', 'Not Set')}", flush=True)
print(f"DB_HOST: {os.environ.get('DB_HOST', 'Not Set')}", flush=True)
print("==================================================================", flush=True)

try:
    # وارد کردن تابع کاربردی جنگو
    from django.core.wsgi import get_wsgi_application
    
    # ساخت و بازگرداندن اپلیکیشن WSGI
    application = get_wsgi_application()
    print("Django WSGI application loaded successfully", flush=True)
except Exception as e:
    print(f"Error loading Django WSGI application: {e}", flush=True)
    import traceback
    traceback.print_exc()
    
    # حتی اگر جنگو بارگذاری نشد، یک تابع ساده WSGI برای تست ارائه می‌دهیم
    def application(environ, start_response):
        status = '200 OK'
        output = f'Django WSGI application failed to load: {e}'.encode('utf-8')
        response_headers = [('Content-type', 'text/plain; charset=utf-8'),
                            ('Content-Length', str(len(output)))]
        start_response(status, response_headers)
        return [output] 