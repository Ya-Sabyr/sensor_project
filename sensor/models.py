from django.db import models

# Create your models here.

class City(models.Model):
    city_name = models.CharField(max_length=40)
    sensors_number = models.IntegerField()
    
class District(models.Model):
    district_name = models.CharField(max_length=40)
    sensors_number = models.IntegerField()

class Company(models.Model):
    ...

class Sensor(models.Model):
    created_time = models.TimeField(verbose_name= "Time when sensor was set up" , auto_now_add=True)
    modified_time = models.TimeField(verbose_name= "Time when something in it was changed")
    company = models.ForeignKey(Company, on_delete= models.CASCADE, verbose_name= "The sensor it is related to")
    city = models.ForeignKey(City, on_delete=models.CASCADE, verbose_name= "The city it is located at")
    district = models.ForeignKey(District, on_delete=models.CASCADE, verbose_name= "The area it is located at")
    address = models.CharField(verbose_name= "The place where it was installed", max_length=100)