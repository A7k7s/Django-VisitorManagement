from django.shortcuts import render,redirect
from django.urls import path, include
from .views import home
urlpatterns = [
    path('', home, name='home'),
]