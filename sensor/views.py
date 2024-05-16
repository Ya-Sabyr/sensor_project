from django.shortcuts import render
from .models import City, District, Sensor
from reports.models import Record

# Create your views here.
def district_list_view(request):
    districts = District.objects.all()
    context = {'districts': districts}
    return render(request, 'sensor/index.html', context)

def district_view(request, district):
    sensors = Sensor.objects.filter(district=district)
    sensor_data = []
    for sensor in sensors:
        latest_record = Record.objects.filter(sensor__address=sensor.address).order_by('-time').first()
        is_full = latest_record.full if latest_record else False
        sensor_data.append({'sensor': sensor, 'is_full': is_full})
    return render(request, 'sensor/district.html', {'sensors': sensor_data})

