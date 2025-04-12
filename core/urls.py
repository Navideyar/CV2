from django.urls import path
from . import views

app_name = 'main_core'

urlpatterns = [
    path("", views.index, name="index"),
    path('policy/', views.policy, name='policy'),
    path('policy-and-privacy/', views.policy, name='policy'),
    path('about-me/', views.about, name='about' ),
    path('personal-website/', views.personal_website, name='personal_website'),
    path('corporate-website/', views.corporate_website, name='corporate_website'),
    path('ecommerce-website/', views.ecommerce_website, name='ecommerce_website'),
    path('testimonials/', views.testimonials, name='testimonials'),
]

