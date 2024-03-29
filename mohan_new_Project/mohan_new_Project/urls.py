"""mohan_new_Project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from practicedjango_1 import views as pd1
from Jobs_Assignment import views as ja
from do_your_work import views as dw



urlpatterns = {
    path('admin/', admin.site.urls),
    path('hello/', pd1.welcome),
    path('hyd', ja.hyd_jobs),
    path('bang', ja.bang_jobs),
    path('pune', ja.pune),
    path('work', dw.time_waste),
}

