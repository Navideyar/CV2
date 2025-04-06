# راهنمای تنظیمات دیتابیس

## محیط توسعه (Development)

در محیط توسعه، پروژه به صورت پیش‌فرض از SQLite استفاده می‌کند:

```python
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}
```

این تنظیمات در فایل `cv2/setting/development.py` قرار دارد و به‌صورت خودکار در هنگام اجرای 
پروژه در محیط توسعه استفاده می‌شود.

## محیط تولید (Production)

در محیط تولید، پروژه از PostgreSQL استفاده می‌کند. تنظیمات دیتابیس به شرح زیر است:

```python
# تنظیمات از طریق DATABASE_URL
DATABASE_URL = os.environ.get('DATABASE_URL')
if DATABASE_URL:
    DATABASES = {'default': dj_database_url.config(default=DATABASE_URL)}
else:
    # تنظیمات از طریق متغیرهای محیطی جداگانه
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': os.environ.get('DB_NAME', 'postgres'),
            'USER': os.environ.get('DB_USER', ''),
            'PASSWORD': os.environ.get('DB_PASSWORD', ''),
            'HOST': os.environ.get('DB_HOST', 'localhost'),
            'PORT': os.environ.get('DB_PORT', '5432'),
            'OPTIONS': {
                'client_encoding': 'UTF8',
            },
        }
    }
```

این تنظیمات در فایل `cv2/setting/production.py` قرار دارد.

## تنظیمات متغیرهای محیطی

برای تنظیم متغیرهای محیطی، می‌توانید از فایل `.env.production` استفاده کنید:

```
# تنظیمات دیتابیس به یکی از دو روش زیر
DATABASE_URL=postgres://username:password@host:port/database_name

# یا به صورت جداگانه
DB_NAME=postgres
DB_USER=root
DB_PASSWORD=your_password
DB_HOST=database_host
DB_PORT=5432
```

سپس با دستور زیر این تنظیمات را در محیط تولید فعال کنید:

```bash
cp .env.production .env
```

## نکات مهم:

1. **نصب درایور PostgreSQL**: مطمئن شوید که پکیج `psycopg2` یا `psycopg2-binary` نصب شده باشد:
   ```
   pip install psycopg2-binary
   ```

2. **مهاجرت دیتابیس**: پس از تنظیم دیتابیس، دستورات مهاجرت را اجرا کنید:
   ```
   python manage.py migrate
   ```

3. **امنیت**: اطلاعات حساس مانند رمز عبور دیتابیس را هرگز در مخزن کد ذخیره نکنید. 