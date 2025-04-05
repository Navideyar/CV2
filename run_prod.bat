@echo off
REM تنظیم متغیر محیطی برای محیط تولید
set DJANGO_ENV=production

REM بارگذاری متغیرهای محیطی از فایل .env.prod با استفاده از اسکریپت پایتون
python load_env.py .env.prod

REM اجرای سرور جنگو
python manage.py runserver 