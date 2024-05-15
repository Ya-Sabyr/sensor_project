from django.shortcuts import render
from .models import Record

# Create your views here.
def records_view(request):
    records = Record.objects.all()
    return render(request, 'reports/reports.html', {'records': records})