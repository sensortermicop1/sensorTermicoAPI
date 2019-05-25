from django.shortcuts import render

# Create your views here.


def sensor(request):
    istekler = SensorInformation.objects.all()
    return render(request, 'list.html', locals())