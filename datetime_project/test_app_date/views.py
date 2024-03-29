from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime


# Create your views here.
def datetimeinfo(request):
    date = datetime.now()
    h = int(date.strftime("%H"))  # to get the time in hours
    msg = "<h1> Hello Guest"
    if h < 12:
        msg = msg + "Good Morning"

    elif h < 16:
        msg = msg + "Good Afternoon!!!"

    elif h < 21:
        msg = msg + "Good Evening!!!"

    else:
        msg = msg + "Good Night!!!"

    msg = msg + "</h1><hr>"
    msg = msg + "<h1> Now server time is: " + str(date) + "</h1>"
    return HttpResponse(msg)

# We use this to display current server time and wish the guest
