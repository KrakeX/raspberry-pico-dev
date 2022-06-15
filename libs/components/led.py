from machine import Pin

class Led():
    pin = int
    instance = Pin
    
    def __init__(self, pinNumber = 25):
        self.pin = pinNumber
        self.instance = Pin(self.pin, Pin.OUT)
        print(f'Led init successfuly on pin {self.pin}') 

    def ledOn(self):
        self.instance.value(True)

    def ledOff(self):
        self.instance.value(False)
