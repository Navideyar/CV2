import os
from pathlib import Path

# تشخیص محیط اجرا
ENVIRONMENT = os.environ.get('DJANGO_ENVIRONMENT', 'development')

# بارگذاری تنظیمات مناسب بر اساس محیط
if ENVIRONMENT == 'production':
    from cv2.setting.production import *
else:
    from cv2.setting.development import *

print(f"Django running in {ENVIRONMENT} mode.") 