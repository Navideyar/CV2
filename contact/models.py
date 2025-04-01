from django.db import models
from django.contrib.auth.models import User

class Contact(models.Model):
    name = models.CharField(max_length=250)
    email = models.EmailField()
    message = models.TextField()
    subject = models.CharField(max_length=250 , default='بدون موضوع')
    phone = models.CharField(max_length=250 , default='بدون شماره تلفن', null=True, blank=True) 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['-created_at']
        
        

