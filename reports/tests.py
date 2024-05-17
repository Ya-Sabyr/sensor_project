from django.test import TestCase, Client
from django.urls import reverse
from .models import RecordProxy
from sensor.models import Sensor, City, District
# Create your tests here.

class RecordViewTests(TestCase):
    def setUp(self) -> None:
        self.city = City.objects.create(city_name='Test city')
        self.district = District.objects.create(district_name='Test district', city=self.city)
        self.sensor = Sensor.objects.create(city=self.city, district=self.district, address='Test address')
        self.record = RecordProxy.objects.create(sensor=self.sensor, distance=11.4, full=True)
        self.client = Client()
        
    def test_records_view(self):
        response = self.client.get(reverse('reports:reports'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'reports/reports.html')
        self.assertContains(response, self.record.sensor.address)
    
    def test_record_delete_view(self):
        response = self.client.post(reverse('reports:delete', args=[self.record.id]))
        self.assertRedirects(response, reverse('reports:reports'))
        self.assertFalse(RecordProxy.objects.filter(id=self.record.id).exists())