from machine import Pin
import utime


class Led():
    pin = int
    instance = Pin

    def __init__(self, pinNumber=25):
        self.pin = pinNumber
        self.instance = Pin(self.pin, Pin.OUT)
        print(f'Led init successfuly on pin {self.pin}')

    def on(self):
        self.instance.value(True)

    def off(self):
        self.instance.value(False)

    def working(self):
        self.on()
        utime.sleep(0.1)
        self.off()
        utime.sleep(0.1)
