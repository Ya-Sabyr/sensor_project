from django.shortcuts import render
from .models import City, District, Sensor

# Create your views here.
def district_list_view(request):
    districts = District.objects.all()
    return render(request, 'sensor/index.html', {'districts': districts})

def district_view(request, district):
    sensors = Sensor.objects.filter(district=district)
    return render(request, 'sensor/district.html', {'sensors': sensors})

