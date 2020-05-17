from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.Home, name='bets-home'),
    path('increment/', views.Increment, name='increment'),
    path('decrement/', views.Decrement, name='decrement'),
    path('getcoins/', views.getCoins, name='getcoins'),
    path('cards/', views.Cards, name='cards'),
]
