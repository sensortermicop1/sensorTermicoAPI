from django.shortcuts import get_object_or_404
from .models import Measurement, SensorInformation
from django_cron import CronJobBase, Schedule
from bs4 import BeautifulSoup
import requests
import datetime
from django.core.mail import send_mail


class GetTemperatureCron(CronJobBase):
    RUN_EVERY_MINS = 120 # every 2 hours

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'sensor.get_temperature_cron'    # a unique code

    def do(self):
        page = requests.get('http://192.168.0.13/')
        soup = BeautifulSoup(page.text , 'html.parser')
        temp = float(soup.get_text())
        time = datetime.datetime.now()
        sensor = get_object_or_404(SensorInformation, pk = 1)
        measurement = Measurement.objects.create_measurement(sensor, temp, time)
        if temp > sensor.maxTemperature or temp < sensor.minTemperature:
            send_mail('Temperatura anômala no sistema',
            'Foi detectada uma temperatura anômala.',
            'teste@example.com',
            ['sensortermicopi1@gmail.com'],
            fail_silently=False,)
        elif temp == -173.00: # valor retornado pela ESP quando há erro de conexão
            send_mail(
            'Erro de comunicação no sistema',
            'Houve um erro na conexão do sistema. Favor verificar.',
            'teste@example.com',
            ['sensortermicopi1@gmail.com'],
            fail_silently=False,)
