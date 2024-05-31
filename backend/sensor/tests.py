from django.test import TestCase, Client
from django.urls import reverse
from .models import City, District, Sensor
from reports.models import RecordProxy

# Create your tests here.
class SensorViewTests(TestCase):
    def setUp(self) -> None:
        self.city = City.objects.create(city_name='Test city')
        self.district = District.objects.create(district_name='Test district', city=self.city)
        self.sensor = Sensor.objects.create(city=self.city, district=self.district, address='Test address')
        self.record = RecordProxy.objects.create(sensor=self.sensor, distance=11.4, full=True)
        self.client = Client()
        
    def test_district_list_view(self):
        response = self.client.get(reverse('sensors:districts_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'sensor/index.html')
        
    def test_district_view(self):
        response = self.client.get(reverse('sensors:district', args=[self.district.id]))
        self.assertTemplateUsed(response, 'sensor/district.html')
        self.assertContains(response, self.sensor.address)