from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def good_morning(request):
    s = "hello world, chaduvukooo bbey"
    return HttpResponse(s)

