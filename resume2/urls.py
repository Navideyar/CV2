from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path("", views.index, name="index"),
    path('policy/', views.policy, name='policy'),
    path('about-me/', views.about, name='about' ),
    path('contact-me/', views.contact, name='contact'),
    path('accounts/login/', views.login_view, name='login'),
    path('accounts/logout/', views.logout_view, name='logout'),
    path('accounts/signup/', views.signup_view, name='signup'),
    path('accounts/password_reset/', views.password_reset_view, name='password_reset'),

]

