from django.contrib import admin
from .models import Measurement, SensorInformation, System, Product 
# Register your models here.

admin.site.register(Measurement)
admin.site.register(SensorInformation)
admin.site.register(System)
admin.site.register(Product)