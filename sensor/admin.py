from django.contrib import admin
from .models import City, District, Sensor
# Register your models here.

class CityAdmin(admin.ModelAdmin):
    model = City
    
    
class DistrictAdmin(admin.ModelAdmin):
    model = District
    
    
class SensorAdmin(admin.ModelAdmin):
    model = Sensor
    
    
admin.site.register(City, CityAdmin)
admin.site.register(District, DistrictAdmin)
admin.site.register(Sensor, SensorAdmin)