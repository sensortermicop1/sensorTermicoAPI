from django.shortcuts import render
from django.http import HttpResponse
from .models import Measurement

# Create your views here.

def index(request):
    latest_measurement_list =  Measurement.objects.order_by('-finalTime')[:5]
    output = ', '.join([str(m.temperature) for m in latest_measurement_list])
    return HttpResponse(output)

def detail(request, measurement_id):
    return HttpResponse("You're looking at measurement %s." % measurement_id)
