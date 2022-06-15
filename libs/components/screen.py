from machine import I2C, Pin
from libs.dependencies.ssd1306 import SSD1306_I2C

class Screen():
    sda = int
    scl = int
    i2c = I2C
    instance = SSD1306_I2C
     
    def __init__(self, width = 128, height = 64, sda = 8, scl = 9):
        self.sda = sda
        self.scl = scl
        self.width = width
        self.height = height
        self.i2c = I2C(0, scl=Pin(scl), sda=Pin(sda), freq=200000)
        self.instance = SSD1306_I2C(self.width, self.height, self.i2c)
        print("I2C Address      : " + hex(self.i2c.scan()[0]).upper())
        print("I2C Configuration: " + str(self.i2c))

    def clear(self):
        self.instance.fill(0)
    

    def showText(self,message):
        self.clear()
        self.instance.text(message, 3, 8)
        self.instance.show()
