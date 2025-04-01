from django.contrib import admin
from .models import  Contact

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'message', 'created_at', 'updated_at')
    list_filter = ('created_at', 'updated_at')
    search_fields = ('name', 'email', 'subject', 'message')
    list_per_page = 10

admin.site.register(Contact, ContactAdmin)

