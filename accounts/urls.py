from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('accounts/logout/', views.logout_view, name='logout'),
    path('accounts/signup/', views.signup_view, name='signup'),
    path('accounts/password_reset/', views.password_reset_view, name='password_reset'),
]