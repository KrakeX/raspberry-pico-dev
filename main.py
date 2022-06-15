from libs.utils.data import getAverageFromList, maintainAmountOfValuesInList
from libs.components.screen import Screen
from libs.components.led import Led
from libs.components.termometer import Termometer
import utime

# Init LEDS
activityLed = Led()
termometer = Termometer()
screen = Screen()

listOfTemperatures = []

while True:
    screen.clear()
    maintainAmountOfValuesInList(
        listOfTemperatures, termometer.getTemperature())
    screen.showText(f'Temp: {getAverageFromList(listOfTemperatures)}C')

    if (getAverageFromList(listOfTemperatures) >= 29):
        activityLed.working()
    else:
        activityLed.off()

    utime.sleep(0.1)
