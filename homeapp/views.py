from django.http import HttpResponse
from django.shortcuts import render
from requests import request


# Create your views here.


def home(request):
    return render(request,'homeapp/index.html')

def conditions(request):
    return render(request,'homeapp/conditions.html')

def about(request):
    return render(request,'homeapp/about.html')
def contact(request):
    return render(request,'homeapp/contact.html')