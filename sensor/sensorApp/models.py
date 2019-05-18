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
    sensorId = models.IntegerField(blank=False,
                                   primary_key=True,
                                   unique=True,
                                   default=1)

    def get_absolute_url(self):
        return ('sensorId', (),
                {
                   'id': self.sensorId,
                })

    def save(self, *args, **kwargs):
        super(Post, self).save(*args, **kwargs)

    class Meta:
        ordering = ['sensorId']
        def __unicode__(self):
            return self.title



class Measurement(models.Model):

    temperature = models.DecimalField(max_digits=None,
                                      decimal_places=2)
    finalTime = models.DateTimeField(auto_now=False, 
                                     auto_now_add=False)       
    initialTime = models.DateTimeField(auto_now=False, 
                                       auto_now_add=False)
    measurementId = models.IntegerField(blank=False,
                                        primary_key=True,
                                        unique=True,
                                        default=1)

    def get_absolute_url(self):
        return ('measurementId', (),
                {
                   'id': self.measurementId,
                })

    def save(self, *args, **kwargs):
        super(Post, self).save(*args, **kwargs)

    class Meta:
        ordering = ['finalTime']
        def __unicode__(self):
            return self.title



class System(models.Model):
    systemId = models.IntegerField(blank=False,
                                   primary_key=True,
                                   unique=True,
                                   default=1)   
    systemType = models.CharField(max_length=1,
                                  choices=SYSTEM_CHOICES,
                                  blank=True) 

    def get_absolute_url(self):
        return ('systemId', (),
                {
                   'id': self.systemId,
                })

    def save(self, *args, **kwargs):
        super(Post, self).save(*args, **kwargs)

    class Meta:
        ordering = ['systemId']
        def __unicode__(self):
            return self.title

                                  
                                            

class Product(models.Model):
    productName = models.CharField(max_length=100)
    productQuantity = models.IntegerField(blank=False)
    productId = models.IntegerField(blank=False,
                                    primary_key=True,
                                    unique=True,
                                    default=1)

    def get_absolute_url(self):
        return ('productId', (),
                {
                   'id': self.productId,
                })

    def save(self, *args, **kwargs):
        super(Post, self).save(*args, **kwargs)

    class Meta:
        ordering = ['productId']
        def __unicode__(self):
            return self.title


