from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def welcome(request):     #we can use any varibale name in place of request
    s="<h1>Hello Welcome to django classes at Nursery level</h1>"    #by using the <h1> over here we get the text with big letters
    return HttpResponse(s)


