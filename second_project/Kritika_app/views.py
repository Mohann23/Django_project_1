from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime


# Create your views here.
def timeinfo(request):
    date = datetime.now()
    msg = "Good Morning kritika"
    msg = msg + "Now the time is " + str(date)
    return HttpResponse(msg)


def timeinfo_2(request):
    msg = "Good Afternoon"
    return HttpResponse(msg)
