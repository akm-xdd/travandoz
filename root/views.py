from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request,'pages/home.html')

def login(request):
    return render(request,'pages/contact.html')

def about(request):
    return render(request,'pages/about.html')

