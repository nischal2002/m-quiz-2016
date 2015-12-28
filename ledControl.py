from gpiozero import LED
from time import sleep


GREEN_LED_GPIO = 22
RED_LED_GPIO = 17
ON_TIME = 5

greenLed = LED(GREEN_LED_GPIO)
redLed = LED(RED_LED_GPIO)


def greenLedOn( onTime = ON_TIME) :
    greenLed.on()
    print("Switching On Green Led")
    sleep(ON_TIME)
    greenLed.off()
    print("Switching Off Green Led")

def redLedOn(onTime = ON_TIME) :
    redLed.on()
    print("Switching On Red Led")
    sleep(ON_TIME)
    redLed.off()

if __name__ == '__main__':
    greenLedOn()
    redLedOn()

