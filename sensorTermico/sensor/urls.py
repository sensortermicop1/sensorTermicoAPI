from django.urls import path

from . import views

app_name = 'sensor'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:measurement_id>/', views.detail, name='detail'),
    path('detail/<int:sensor_id>', views.sensor_detail, name='sensor_detail'),
    path('measurement/', views.get_data, name='measurement'),
]