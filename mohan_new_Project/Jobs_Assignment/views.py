from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def hyd_jobs(request):
    s = "Jobs in Hyderabad:" \
        "there are so  many jobs in hyderabad" \
        "If you want you can check them through " \
        "different websites plz don' come and " \
        "disturb me Pig..."
    return HttpResponse(s)


def bang_jobs(request):
    s = "Jobs in Bangalore:" \
        "there are so  many jobs in Bangalore" \
        "If you want you can check them through " \
        "different websites plz don' come and " \
        "disturb me Pig..."
    return HttpResponse(s)

def pune(request):
    s = "Jobs in pune:" \
        "there are so  many jobs in pune" \
        "If you want you can check them through " \
        "different websites plz don' come and " \
        "disturb me Pig..."
    return HttpResponse(s)
