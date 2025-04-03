from django.shortcuts import render, redirect
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.utils.translation import gettext as _
import random
import string
from django.conf import settings

# Create your views here.   
def login_view(request):
    if request.user.is_authenticated:
        return redirect('main_core:index')
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                # بررسی گزینه "مرا به خاطر بسپار"
                remember_me = request.POST.get('remember_me', None)
                if remember_me:
                    # اگر کاربر گزینه "مرا به خاطر بسپار" را انتخاب کرده باشد، سشن به مدت ۳۰ روز باقی می‌ماند
                    request.session.set_expiry(2592000)  # 30 days in seconds
                else:
                    # در غیر این صورت، سشن با بستن مرورگر پاک می‌شود
                    request.session.set_expiry(0)
                
                login(request, user)
                return redirect('main_core:index')
            else:
                messages.error(request, 'نام کاربری یا رمز عبور اشتباه است')
    form = AuthenticationForm()
    context = {
        'form': form
    }
    return render(request, 'accounts/login.html', context)

def logout_view(request):
    logout(request)
    return redirect('main_core:index')

def generate_captcha_code(length=6):
    """تولید کد کپچای تصادفی"""
    chars = string.ascii_letters + string.digits
    return ''.join(random.choice(chars) for _ in range(length))

def signup_view(request):
    if request.user.is_authenticated:
        messages.error(request, 'شما قبلا وارد حساب کاربری خود شدید')
        return redirect('main_core:index')
    
    # تولید کد کپچا برای درخواست‌های GET
    captcha_code = generate_captcha_code()
    
    if request.method == 'POST':
        # بررسی کپچا
        captcha_input = request.POST.get('captcha_input')
        server_captcha = request.POST.get('server_captcha')
        
        # اگر کپچا نادرست بود، پیام خطا نمایش داده شود
        if not captcha_input or captcha_input != server_captcha:
            messages.error(request, 'کد امنیتی وارد شده نادرست است.')
            # تولید کپچای جدید
            return render(request, 'accounts/signup.html', {'captcha_code': generate_captcha_code()})
        
        # بررسی پذیرش قوانین
        terms_accepted = request.POST.get('terms_accepted')
        if not terms_accepted:
            messages.error(request, 'لطفاً شرایط و قوانین سایت را بپذیرید.')
            return render(request, 'accounts/signup.html', {'captcha_code': generate_captcha_code()})
        
        # دریافت اطلاعات فرم
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        
        # بررسی نام کاربری
        if not username:
            messages.error(request, 'لطفاً نام کاربری خود را وارد کنید.')
            return render(request, 'accounts/signup.html', {'captcha_code': generate_captcha_code()})
        
        # بررسی تکراری بودن نام کاربری
        if User.objects.filter(username=username).exists():
            messages.error(request, 'این نام کاربری قبلاً ثبت شده است.')
            return render(request, 'accounts/signup.html', {'captcha_code': generate_captcha_code()})
            
        # بررسی صحت رمز عبور
        if not password1:
            messages.error(request, 'لطفاً رمز عبور را وارد کنید.')
            return render(request, 'accounts/signup.html', {'captcha_code': generate_captcha_code()})
            
        if len(password1) < 8:
            messages.error(request, 'رمز عبور باید حداقل 8 کاراکتر باشد.')
            return render(request, 'accounts/signup.html', {'captcha_code': generate_captcha_code()})
        
        try:
            # ایجاد کاربر جدید با نام کاربری مشخص شده و ایمیل خالی
            user = User.objects.create_user(username=username, email='', password=password1)
            user.save()
            
            # ورود به سیستم
            user = authenticate(username=username, password=password1)
            if user is not None:
                login(request, user)
                messages.success(request, f'حساب کاربری شما با نام کاربری {username} با موفقیت ایجاد شد و اکنون وارد سیستم شده‌اید.')
                return redirect('main_core:index')
        except Exception as e:
            messages.error(request, f'خطا در ایجاد حساب کاربری: {str(e)}')
            return render(request, 'accounts/signup.html', {'captcha_code': generate_captcha_code()})
    
    # ارسال کد کپچای جدید به قالب
    return render(request, 'accounts/signup.html', {'captcha_code': captcha_code})