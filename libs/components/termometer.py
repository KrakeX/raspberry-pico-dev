from machine import ADC

class Termometer():
    pin=int
    instance = ADC
    def __init__(self,pin = 4):
        self.pin = pin
        self.instance = ADC(self.pin)
        print(f'Termometer init successfuly on pin {self.pin}') 
        
    def getReading(self):
        conversion_factor = 3.3 / 65535
        return self.instance.read_u16() * conversion_factor

    def getTemperature(self):
        return round(27 - (self.getReading() - 0.706) / 0.001721, 2)
    
    
