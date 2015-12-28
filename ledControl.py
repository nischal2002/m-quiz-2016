from gpiozero import LED
from time import sleep


GREEN_LED_GPIO = 27
RED_LED_GPIO = 17
BUZZER_GPIO = 22 
LED_ON_TIME = 5
BUZZER_ON_TIME = 5

greenLed = LED(GREEN_LED_GPIO)
redLed = LED(RED_LED_GPIO)
buzzer = LED(BUZZER_GPIO)


def greenLedOn( onTime = LED_ON_TIME) :
    greenLed.on()
    print("Switching On Green Led")
    sleep(onTime)
    greenLed.off()
    print("Switching Off Green Led")

def redLedOn(onTime = LED_ON_TIME) :
    redLed.on()
    print("Switching On Red Led")
    sleep(onTime)
    redLed.off()

def buzzerOn(onTime = BUZZER_ON_TIME) :
    buzzer.on();
    sleep(onTime) 
    buzzer.off();

def buzzerPulse(numOfPulses, pulseTime):
    while numOfPulses > 0:
        print("Switching On Buzzer")
       	buzzerOn(pulseTime/2)
       	sleep(pulseTime/2)
       	numOfPulses = numOfPulses - 1;  
     

if __name__ == '__main__':
    redLedOn()	
    greenLedOn()
    buzzerPulse(5,1)

    

