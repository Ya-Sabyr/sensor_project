from django.db import models

# Create your models here.

class City(models.Model):
    city_name = models.CharField(max_length=100)
    sensors_number = models.IntegerField(default=0)
    
class District(models.Model):
    district_name = models.CharField(max_length=100)
    sensors_number = models.IntegerField(default=0)
    сity = models.ForeignKey(City, on_delete=models.CASCADE)

"""
class Company(models.Model):
    name = models.CharField(max_length=100)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
"""

class Sensor(models.Model):
    created_at = models.TimeField(verbose_name= "Time when sensor was set up" , auto_now_add=True)
    modified_at = models.TimeField(verbose_name= "Time when something in it was changed", auto_now=True)
#    company = models.ForeignKey(Company, on_delete= models.CASCADE, verbose_name= "The sensor it is related to")
    city = models.ForeignKey(City, on_delete=models.CASCADE, verbose_name= "The city it is located at")
    district = models.ForeignKey(District, on_delete=models.CASCADE, verbose_name= "The area it is located at")
    address = models.CharField(verbose_name= "The address where it was installed", max_length=100)