from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse

def index(request):
    return render(request,"unauthorized.html")
def login(request):
    return render(request,"login.html")
def register(request):
    return render(request,"register.html")


