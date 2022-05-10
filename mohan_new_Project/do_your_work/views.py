from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def time_waste(request):
    s = "Arey silly fellow, don't waste the time, time is more precisious, Have a good day"
    return HttpResponse(s)
