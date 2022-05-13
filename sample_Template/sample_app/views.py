from django.shortcuts import render
from datetime import datetime


# Create your views here.
def sam_app(request):
    date = datetime.now()
    my_d = {'My_date': date}
    return render(request, 'sample_app/wish.html', context=my_d)
