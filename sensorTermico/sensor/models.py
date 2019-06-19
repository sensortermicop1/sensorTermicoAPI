import datetime

from django.contrib.auth.models import User
from django.db import models

# Create your models here.

SYSTEM_CHOICES = (
    (None, 'Null'),
    ('F', 'Frio'),
    ('Q', 'Quente')
)

class System(models.Model):
    systemId = models.IntegerField(blank=False,
                                   primary_key=True,
                                   unique=True,
                                   default=1)   
    systemType = models.CharField(max_length=1,
                                  choices=SYSTEM_CHOICES,
                                  blank=True) 



class SensorInformation(models.Model):

    maxTemperature = models.DecimalField(max_digits=5, 
                                         decimal_places=2)
    minTemperature = models.DecimalField(max_digits=5, 
                                         decimal_places=2)
    sensorId = models.IntegerField(blank=False,
                                   primary_key=True,
                                   unique=True,
                                   default=1)
    localization = models.ForeignKey(System, on_delete=models.CASCADE)


class Measurement(models.Model):
    sensor = models.ForeignKey(SensorInformation, on_delete=models.CASCADE)
    temperature = models.DecimalField(max_digits=5,
                                      decimal_places=2)
    time = models.DateTimeField(auto_now=False, 
                                     auto_now_add=False)       
    measurementId = models.IntegerField(blank=False,
                                        primary_key=True,
                                        unique=True,
                                        default=1)
                                  
                                            

class Product(models.Model):
    productName = models.CharField(max_length=100)
    productQuantity = models.IntegerField(blank=False)
    productId = models.IntegerField(blank=False,
                                    primary_key=True,
                                    unique=True,
                                    default=1)
