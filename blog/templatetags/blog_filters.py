from django import template
from django.utils.html import strip_tags
from django.utils.encoding import force_str
from django.utils.safestring import mark_safe
import re
import html

register = template.Library()

@register.filter
def clean_text_excerpt(value, length=100):
    """
    این فیلتر تگ‌های HTML را حذف می‌کند، کاراکترهای خاص را پاک می‌کند
    و متن را به اندازه مشخص شده کوتاه می‌کند
    """
    if not value:
        return ""
    
    # تبدیل به رشته معمولی
    text = force_str(value)
    
    # حذف تگ‌های HTML
    text = strip_tags(text)
    
    # تبدیل کدهای HTML مثل &nbsp; به کاراکترهای واقعی
    text = html.unescape(text)
    
    # حذف کاراکترهای اضافی و فاصله‌های زیاد
    text = re.sub(r'\s+', ' ', text)
    text = text.strip()
    
    # کوتاه کردن متن
    if len(text) <= length:
        return text
    else:
        return text[:length] + '...' 