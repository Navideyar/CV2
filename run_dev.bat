@echo off
REM تنظیم متغیر محیطی برای محیط توسعه
set DJANGO_ENV=development

REM بارگذاری متغیرهای محیطی از فایل .env.dev با استفاده از اسکریپت پایتون
python load_env.py .env.dev

REM اجرای سرور توسعه جنگو
python manage.py runserver 