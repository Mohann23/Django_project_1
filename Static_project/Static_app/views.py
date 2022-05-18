from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'Static_app/home.html')

def profile(request):
    return render(request,'Static_app/profile.html')
