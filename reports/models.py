from django.db import models
from sensor.models import Sensor, City, District
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

# Create your models here.
class Record(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE)
    distance = models.FloatField()
    time = models.DateTimeField(auto_now_add=True)
    full = models.BooleanField(default=True)
    
    class Meta:
        verbose_name = 'Запись'
        ordering = ['-time']

    def __str__(self):
        return f"{self.time.strftime('%Y-%m-%d %H:%M:%S')}"
    
@receiver(post_save, sender=Record)
def update_bins_count(sender, instance, **kwargs):
    if instance.full:
        instance.sensor.district.full_bins += 1
        instance.sensor.city.full_bins += 1
    else:
        instance.sensor.district.full_bins -= 1
        instance.sensor.city.full_bins -= 1
    instance.sensor.district.save()
    instance.sensor.city.save()
    
@receiver(post_delete, sender=Record)
def delete_bins_count(sender, instance, **kwargs):
    if instance.full:
        instance.sensor.district.full_bins -= 1
        instance.sensor.city.full_bins -= 1
        
        
class RecordManager(models.Manager):
    def get_queryset(self):
        return super(RecordManager, self).get_queryset().filter(full=True)
    

class RecordProxy(Record):
    objects = RecordManager()
    
    class Meta:
        proxy = True