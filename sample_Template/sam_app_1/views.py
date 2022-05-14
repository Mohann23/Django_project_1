from django.shortcuts import render
from datetime import datetime

# Create your views here.
def sa_app(request):
    date = datetime.now()
    my_time = {"My_date":date}
    return render(request,'sam_app_1/wish.html',context=my_time)
