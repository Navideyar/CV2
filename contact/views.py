from django.shortcuts import render, redirect
from .forms import ContactForm
from django.contrib import messages
import random
import string


def generate_captcha_code(length=5):
    """تولید کد کپچای تصادفی با طول مشخص"""
    characters = string.ascii_uppercase + string.digits
    # حذف کاراکترهایی که ممکن است با هم اشتباه شوند
    characters = characters.replace('0', '').replace('O', '').replace('1', '').replace('I', '')
    return ''.join(random.choice(characters) for _ in range(length))


def contact(request):
    # تولید کد کپچای تصادفی
    captcha_code = generate_captcha_code()
    
    if request.method == 'POST':
        form = ContactForm(request.POST)
        # بررسی اعتبار کپچا
        server_captcha = request.POST.get('server_captcha', '')
        user_captcha = request.POST.get('captcha_input', '')
        
        # اگر کپچا نادرست بود
        if user_captcha.upper() != server_captcha.upper():
            messages.error(request, "کد امنیتی وارد شده صحیح نیست.")
            context = {
                'form': form,
                'is_authenticated': request.user.is_authenticated,
                'captcha_code': captcha_code
            }
            return render(request, 'contact-me.html', context)
            
        if form.is_valid():
            try:
                form.save()
                return redirect('contact:contact_success')
            except Exception as e:
                messages.error(request, f"خطا در ذخیره‌سازی فرم: {str(e)}")
        else:
            # نمایش خطاهای فرم
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"خطا در فیلد {field}: {error}")
    else:
        # اگر کاربر لاگین بود، فیلدهای نام و ایمیل را پر کن
        if request.user.is_authenticated:
            initial_data = {
                'name': request.user.get_full_name() or request.user.username,
                'email': request.user.email
            }
            form = ContactForm(initial=initial_data)
        else:
            form = ContactForm()
    
    # ارسال وضعیت لاگین کاربر و کد کپچا به قالب
    context = {
        'form': form,
        'is_authenticated': request.user.is_authenticated,
        'captcha_code': captcha_code
    }
    return render(request, 'contact-me.html', context)

def contact_success(request):
    return render(request, 'contact-success.html')
