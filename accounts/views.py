from django.shortcuts import render, redirect
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages

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


def signup_view(request):
    form = UserCreationForm()
    context = {
        'form': form
    }
    return render(request, 'accounts/signup.html', context)
        
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # ورود خودکار پس از ثبت‌نام
            messages.success(request, 'حساب کاربری شما با موفقیت ایجاد شد!')
            return redirect('main_core:index')
        else:
            for field in form:
                for error in field.errors:
                    messages.error(request, f"{field.label}: {error}")
    else:
        form = UserCreationForm()   
    return render(request, 'accounts/signup.html', {'form': form})
