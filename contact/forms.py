from django import forms
from .models import Contact
from captcha.fields import CaptchaField

class ContactForm(forms.ModelForm):
    captcha = CaptchaField(label='کد امنیتی')
    class Meta:
        model = Contact
        fields = ['name', 'email', 'message', 'subject' , 'phone']
    
