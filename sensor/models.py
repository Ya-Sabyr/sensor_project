from django.db import models

# Create your models here.

class City(models.Model):
    city_name = models.CharField(max_length=100)
    sensors_number = models.IntegerField(default=0)
    full_bins = models.IntegerField(default=0)
    
    def __str__(self) -> str:
        return self.city_name
    
class District(models.Model):
    district_name = models.CharField(max_length=100)
    sensors_number = models.IntegerField(default=0)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    full_bins = models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.district_name
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
    address = models.CharField(verbose_name= "The address where it was installed", max_length=100, default=None)
    coordinate_1 = models.CharField(max_length=50, default=None)
    coordinate_2 = models.CharField(max_length=50, default=None)
    
    def __str__(self) -> str:
        return f'{self.id}, {self.address}'