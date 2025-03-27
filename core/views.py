from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    return render(request, "index.html")

def about(request):
    return render(request, "about-me.html")

def contact(request):
    return render(request, "contact.html")


def policy(request):
    return render(request, 'policy-and-privacy.html')

def contact(request):
    return render(request, 'contact-me.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('index')  # یا به صفحه اصلی برگردانید
        else:
            # ارسال پیام خطا به کاربر
            messages.error(request, 'نام کاربری یا رمز عبور اشتباه است')
            
    return render(request, 'accounts/login.html')

def logout_view(request):
    logout(request)
    return redirect('index')  # یا به صفحه اصلی برگردانید

def signup_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        
        error = None
        
        # بررسی خالی نبودن فیلدها
        if not username or not email or not password1 or not password2:
            error = 'لطفاً تمام فیلدها را پر کنید'
        # بررسی یکسان بودن رمزها
        elif password1 != password2:
            error = 'رمزهای عبور مطابقت ندارند'
        # بررسی طول رمز عبور
        elif len(password1) < 8:
            error = 'رمز عبور باید حداقل ۸ کاراکتر باشد'
        # بررسی تکراری نبودن نام کاربری
        elif User.objects.filter(username=username).exists():
            error = 'این نام کاربری قبلاً استفاده شده است'
        # بررسی تکراری نبودن ایمیل
        elif User.objects.filter(email=email).exists():
            error = 'این آدرس ایمیل قبلاً استفاده شده است'
            
        if error:
            messages.error(request, error)
            return render(request, 'accounts/signup.html')
        else:
            # ایجاد کاربر جدید
            user = User.objects.create_user(username=username, email=email, password=password1)
            # ورود کاربر
            login(request, user)
            messages.success(request, 'ثبت‌نام شما با موفقیت انجام شد!')
            return redirect('index')  # هدایت به صفحه اصلی
            
    return render(request, 'accounts/signup.html')

def password_reset_view(request):
    return render(request, 'accounts/password-reset.html')

def personal_website(request):
    return render(request, 'services/personal-website.html')

def corporate_website(request):
    return render(request, 'services/corporate-website.html')

def ecommerce_website(request):
    return render(request, 'services/ecommerce-website.html')

def testimonials(request):
    return render(request, 'services/testimonials.html')

def blog(request):
    return render(request, 'blog/index.html')



