from django.shortcuts import render, redirect
from .models import Record

# Create your views here.
def records_view(request):
    records = Record.objects.all()
    return render(request, 'reports/reports.html', {'records': records})

def record_delete(request, record_id):
    if request.method == 'POST':
        record = Record.objects.get(id=record_id)
        record.delete()
    return redirect('reports:reports')