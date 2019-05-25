from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def sensor(request):
    istekler = SensorInformation.objects.all()
    return render(request, 'list.html', locals())