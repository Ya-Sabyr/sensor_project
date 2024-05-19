import os
import django
import serial
import requests
from django.urls import reverse
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'device.settings')
django.setup()

portVar = "port value"

def read_from_device():
    serialInst = serial.Serial(portVar, 9600, timeout=1)
    serialInst.flush()

    while True:
        if serialInst.in_waiting() > 0:
            packet = serialInst.readline().decode('utf-8').rstip()  #distance
            send_to_django(packet)
            
def send_to_django(data):
    url = reverse('reports:receivep')
    full_url = f"http://{settings.ALLOWED_HOSTS[0]}{url}"
    payload = {'data': data}
    response = requests.post(full_url, data=payload)
    
if __name__ == '__main__':
    read_from_device()