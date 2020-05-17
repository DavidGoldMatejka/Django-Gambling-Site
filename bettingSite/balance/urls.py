from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('deposit/', views.Deposit, name='deposit'),
    path('withdraw/', views.Withdraw, name='withdraw'),
]
