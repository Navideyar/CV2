from django import template
from django.utils.html import strip_tags
from django.utils.safestring import mark_safe
import re
import html

register = template.Library()

@register.filter(name='clean_text_excerpt')
def clean_text_excerpt(value, length=100):
    """
    حذف تگ‌های HTML و سپس کاراکترهای خاص HTML را به متن معمولی تبدیل می‌کند
    و در نهایت متن را به طول مشخص‌شده محدود می‌کند.
    """
    if not value:
        return ""
    
    # حذف تگ‌های HTML
    text = strip_tags(value)
    
    # تبدیل کاراکترهای خاص HTML مانند &nbsp; به کاراکترهای معمولی
    text = html.unescape(text)
    
    # حذف فاصله‌های اضافی
    text = re.sub(r'\s+', ' ', text).strip()
    
    # محدود کردن طول متن
    if len(text) > length:
        text = text[:length] + '...'
    
    return text 