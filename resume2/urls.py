from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
     path('policy-and-privacy/', views.policy, name='policy'),
]

