from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse("server is running")

def index(request):
    return render(request,'index.html')

def hello(request,name):
    return HttpResponse("Hello, %s" %name)