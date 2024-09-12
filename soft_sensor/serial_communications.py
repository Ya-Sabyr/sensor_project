import os
import serial
import requests

# Django host and port
DJANGO_HOST = "127.0.0.1"
DJANGO_PORT = "8000"
DJANGO_RECEIVE_ENDPOINT = "receive-device-data/"

# Serial port configuration
portVar = "COM5"  # Port 

def read_from_device():
    serialInst = serial.Serial(portVar, 9600, timeout=1)
    serialInst.flush()

    while True:
        if serialInst.in_waiting > 0:
            packet = serialInst.readline().decode('utf-8').strip()  # distance
            if packet:
                try:
                    distance = float(packet)
                    send_to_django(packet)
                except ValueError:
                    print(f'Received invalid data {packet}')
def send_to_django(data):
    full_url = f"http://{DJANGO_HOST}:{DJANGO_PORT}/{DJANGO_RECEIVE_ENDPOINT}"
    payload = {
        'sensor_id': 1,  # Change to the real id
        'distance': data,
    }
    response = requests.post(full_url, data=payload)
    
    # Debugging
    print("Response status code:", response.status_code)
    print("Response content:", response.content.decode('utf-8'))
    
if __name__ == '__main__':
    read_from_device()