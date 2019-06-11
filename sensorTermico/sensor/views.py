from django.shortcuts import render
from django.http import HttpResponse
from .views import Measurement

# Create your views here.

def index(request):
    return HttpResponse("Hello, world.")