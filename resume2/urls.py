from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('policy/', views.policy, name='policy'),
    path('about-me/', views.about, name='about' ),
    path('contact-me/', views.contact, name='contact'),
    
]

