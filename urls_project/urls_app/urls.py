from django.contrib import admin
from django.urls import path
from urls_app import views

urlpatterns = [
    path('hyd', views.hyd_jobs),
    path('bang', views.bang_jobs),
    path('pune', views.pune),
]
