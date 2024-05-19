from django.urls import path
from .views import records_view, record_delete, receive_device_data

app_name= 'reports'

urlpatterns = [
    path('', records_view, name='reports'),
    path('delete/<int:record_id>/', record_delete, name='delete'),
    path('receive-device-data/', receive_device_data, name='receive'),
]
    