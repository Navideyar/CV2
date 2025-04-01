from django.shortcuts import render, redirect
from .forms import ContactForm
from django.contrib import messages


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
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
        form = ContactForm()
    return render(request, 'contact-me.html', {'form': form})

def contact_success(request):
    return render(request, 'contact-success.html')
