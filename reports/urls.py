from django.urls import path
from .views import records_view, record_delete

app_name= 'reports'

urlpatterns = [
    path('', records_view, name='reports'),
    path('delete/<int:record_id>/', record_delete, name='delete'),
]
    