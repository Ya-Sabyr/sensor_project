from django.shortcuts import render, redirect
from .models import RecordProxy
from sensor.models import Sensor
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages

# Create your views here.
def records_view(request):
    records = RecordProxy.objects.all()
    return render(request, 'reports/reports.html', {'records': records})

def record_delete(request, record_id):
    if request.method == 'POST':
        try:    
            record = RecordProxy.objects.get(id=record_id)
            record.delete()
            messages.success(request, 'Record deleted successfully')
        except RecordProxy.DoesNotExist:
            messages.error(request, 'Error occured')
    return redirect('reports:reports')

@csrf_exempt
def receive_device_data(request):
    if request.method == "POST":
        sensor_id = request.POST.get('sensor_id')
        distance = request.POST.get('distance')
        if sensor_id and distance:
            try:
                sensor = Sensor.objects.get(id=sensor_id)
                RecordProxy.objects.create(sensor=sensor, distance=distance, full=True)
                return JsonResponse({'status': 'success', 'message': 'good boy'}, status=200)
            except Sensor.DoesNotExist:
                return JsonResponse({'status': 'error', 'message': 'eshe nemnogo'}, status=404)
            except ValueError:
                return JsonResponse({'status': 'error', 'message': 'Value error'}, status=400)
            except Exception as e:
                return JsonResponse({'status': 'error', 'message': str(e)}, status=400)
        return JsonResponse({'status': 'error', 'message': 'Ty dalbayov'}, status=400)
    return JsonResponse({'status': 'error', 'message': 'Ty pipez tupoy'}, status=405) 