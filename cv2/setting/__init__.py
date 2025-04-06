import os
from pathlib import Path

# تشخیص محیط اجرا
ENVIRONMENT = os.environ.get('DJANGO_ENVIRONMENT', 'development')

# بارگذاری تنظیمات مناسب بر اساس محیط
if ENVIRONMENT == 'production':
    from .production import *
else:
    from .development import *

print(f"Django running in {ENVIRONMENT} mode.") 