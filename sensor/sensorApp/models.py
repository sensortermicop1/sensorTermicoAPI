import datetime

from django.contrib.auth.models import User
from django.db import models

# Create your models here.

SYSTEM_CHOICES = (
    (None, 'Null'),
    ('F', 'Frio'),
    ('Q', 'Quente')
)

class SensorInformation(models.Model):

    maxTemperature = models.DecimalField(max_digits=None, 
                                         decimal_places=2)
    minTemperature = models.DecimalField(max_digits=None, 
                                         decimal_places=2)
    sensorId = models.IntegerField(blank=False)


class Measurement(models.Model):

    temperature = models.DecimalField(max_digits=None,
                                      decimal_places=2)
    finalTime = models.DateTimeField(auto_now=False, 
                                     auto_now_add=False)       
    initialTime = models.DateTimeField(auto_now=False, 
                                       auto_now_add=False)
    measurementId = models.IntegerField(blank=False)


class System(models.Model):
    systemId = models.IntegerField(blank=False)    
    systemType = models.CharField(max_length=1,
                                  choices=VOTE_CHOICES,
                                  blank=True)            

class Product(models.Model):
    productName = models.CharField(max_length=100)
    productQuantity = models.IntegerField(blank=False)
    productId = models.IntegerField(blank=False)

    