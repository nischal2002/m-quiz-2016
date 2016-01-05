LED_ON_TIME = 5
BUZZER_ON_TIME = 5

def greenLedOn( onTime = LED_ON_TIME):
    print('Switching GREEN LED on for '+str(onTime) + ' Seconds')
    
def redLedOn(onTime = LED_ON_TIME):
    print('Switching RED LED on for '+str(onTime) + ' Seconds')
    
def buzzerOn(onTime = BUZZER_ON_TIME): 
    print('Switching BUZZER on for '+str(onTime) + ' Seconds')
    
def buzzerPulse(numOfPulses, pulseTime):
    print('BUZZER Pulses:'+str(numOfPulses)+ ' PulseTime:' + str(pulseTime))
    
def redLedBuzzerOn(onTime = LED_ON_TIME):
    print('Switching RED LED AND BUZZER on for '+str(onTime) + ' Seconds')