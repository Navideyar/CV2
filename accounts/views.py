from django.shortcuts import render

# Create your views here.
def logout_view(request):
    logout(request)
    return redirect('core:index')


def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('core:index')
    else:
        form = UserCreationForm()   
    return render(request, 'accounts/signup.html', {'form': form})


def password_reset_view(request):
    return render(request, 'accounts/password-reset.html')
