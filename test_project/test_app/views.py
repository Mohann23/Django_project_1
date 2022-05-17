from django.shortcuts import render
from datetime import datetime


# Create your views here.
def date_info(request):
    date = datetime.now()
    h = int(date.strftime('%H'))
    msg = ""
    if h < 12:
        msg = "Good Morning"
    elif h < 16:
        msg = "Good Afternoon"
    elif h < 21:
        msg = "Good Evening"
    else:
        msg = "Good Night"

    my_dict = {"date_1": date, "some": msg}
    return render(request, 'test_app/test.html', context=my_dict)
