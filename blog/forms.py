from django import forms
from .models import Comment
from captcha.fields import CaptchaField

class CommentForm(forms.ModelForm):
    captcha = CaptchaField(label='کد امنیتی')
    class Meta:
        model = Comment
        fields = ['name', 'email', 'message', 'subject']
    
