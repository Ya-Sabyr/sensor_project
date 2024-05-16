from django.urls import path
from .views import district_list_view, district_view
app_name = 'sensors'

urlpatterns = [
    path("districts-list/", district_list_view, name='districts_list'),
    path("district/<int:district>/", district_view, name='district'),
]
