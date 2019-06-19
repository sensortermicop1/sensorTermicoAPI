from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Measurement, SensorInformation

# Create your views here.

def index(request):
    latest_measurement_list =  Measurement.objects.order_by('-time')[:5]
    return render(request, "index.html", {'latest_measurement_list' : latest_measurement_list})

def detail(request, measurement_id):
    measurement = get_object_or_404(Measurement, pk = measurement_id)
    return render(request, "sensor/detail.html", {'measurement' : measurement })

def sensor_detail(request, sensor_id):
    sensor = get_object_or_404(SensorInformation, pk = sensor_id)
    return render(request, "sensor/sensor.html", {'sensor' : sensor})