from django.db import models
from sensor.models import Sensor

# Create your models here.
class Record(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE)
    distance = models.FloatField()
    time = models.DateTimeField(auto_now_add=True)
    full = models.BooleanField(default=True)
    
    class Meta:
        verbose_name = 'Запись'
        ordering = ['-time']
        