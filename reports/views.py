from django.shortcuts import render, redirect
from .models import RecordProxy

# Create your views here.
def records_view(request):
    records = RecordProxy.objects.all()
    return render(request, 'reports/reports.html', {'records': records})

def record_delete(request, record_id):
    if request.method == 'POST':
        record = RecordProxy.objects.get(id=record_id)
        record.delete()
    return redirect('reports:reports')