from django.shortcuts import render
from gpiozero import OutputDevice
import os

os.environ["PIGPIO_ADDR"] = '172.24.98.27'
RELAY_PIN=21
relay=OutputDevice(RELAY_PIN,active_high=False,initial_value=False)
LightOff=False

def HomeLight(request):
    global relay,LightOff
    if request.method == 'POST':
        action = request.POST.get('action')
        if action == 'on':
            if(LightOff):
                return render(request, 'HomeLightApp/HomeLight.html')
            else:
                relay=OutputDevice(RELAY_PIN,active_high=False,initial_value=False)
                relay.on()
                LightOff=True
        elif action == 'off':
                relay.close()
                LightOff=False
    os.environ["PIGPIO_ADDR"] = '172.24.98.27'
    return render(request, 'HomeLightApp/HomeLight.html',{'switch':LightOff})