''' This will be the engine which runs the quiz '''
import threading
import select
import sys
import os

if (os.uname().nodename == 'raspberrypi'):
    from ledControl import greenLedOn
    from ledControl import redLedOn
    from ledControl import buzzerOn
    from ledControl import buzzerPulse
    from ledControl import redLedBuzzerOn
else:
    from ledControlNoop import greenLedOn
    from ledControlNoop import redLedOn
    from ledControlNoop import buzzerOn
    from ledControlNoop import buzzerPulse
    from ledControlNoop import redLedBuzzerOn

def buzzer(numOfPulses, totalTime, answeredEvent):
    ''' This will run pulse the buzzer 5 times 1/2 second on , 1/2 second off
        while waiting for the answered event'''
    #print("The Buzzer Thread is started")
    timeToWaitBeforePulsing = (totalTime - numOfPulses) if totalTime > numOfPulses else 0
    if timeToWaitBeforePulsing > 0 :
        answered = answeredEvent.wait(timeToWaitBeforePulsing)
        
    if answered:
        return
    else:
        while numOfPulses > 0:
            buzzerOn(0.5)
            if answeredEvent.wait(0.5):
                break
            else:
                numOfPulses -= 1



def runQuestion(questionText,correctAnswer, timeout):
    print("You have "+str(timeout)+" seconds to answer this question")
    print(questionText)
    ansEvent = threading.Event()
    buzzerThread = threading.Thread(name='buzzerThread', 
                    target=buzzer, args=[5, 10, ansEvent])
    buzzerThread.start()
    answerReady, _, _ = select.select([sys.stdin],[],[],timeout)
    ansEvent.set();
    # above line says that read from stdin and wait for TIMEOUT seconds 
    # If no response for TIMEOUT seconds, then retun false
    if answerReady : # if the answer has been input within the TIMEOUT seconds
    #Let us read the answer and then calculate and see if the answer is correct  
        try:
            answer = int(sys.stdin.readline().strip()) # readline() reads the answer and strip() removes the enter key
            if (answer == correctAnswer): # Here we are checking if the answer is correct or wrong
                return True
            else :
                return False
        except: # If you return a non number, the code will come here
            return False
    else:
        print(" Sorry you have run out of Time to answer the question")
        return False
    
    