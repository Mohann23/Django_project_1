from django.shortcuts import render
from datetime import datetime

# Create your views here.
def temp_view(request):
    date = datetime.now()
    my_Dict = {'my_date':date}
    return render(request,'Template_app/wish.html',context=my_Dict)