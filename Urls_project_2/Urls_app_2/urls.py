from django.contrib import admin
from django.urls import path
from Urls_app_2 import views

urlpatterns = [
    path('gm', views.good_morning),
]
