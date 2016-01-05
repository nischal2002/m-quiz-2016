import random # This allows you to generate random numbers
import select # This allows you to wait for a specific time for input from user
import sys    # this allows you to read the user input from keyboard also called "stdin"

import os # This module is used to check if we are running on pi
import threading

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

TIMEOUT=10  # this is the amount of time you will wait for an answer in Seconds. 10 means 10 seconds
QUESTION_COUNT=10
ANSWER_GOAL=8
LED_ON_TIME=2
BETTER_LUCK_TIME=3



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


def classOneQuiz(): # Class 1
    '''this will the Quiz for CLASS 1'''
    questionCount = 0
    correctAnswers = 0
    while(questionCount < QUESTION_COUNT):
        if (additionQuestionClassOne()) :
            greenLedOn(LED_ON_TIME)
            correctAnswers = correctAnswers + 1
        else:
            redLedBuzzerOn(LED_ON_TIME)
        questionCount = questionCount + 1
    print("You got " + str(correctAnswers) + " correct");
    if(correctAnswers >= ANSWER_GOAL):
        print("congratulations!,you win!!!")
    else :
        print("sorry,better luck next time:)")
        redLedBuzzerOn(BETTER_LUCK_TIME)
          




def additionQuestionClassOne(): #class 1
    ''' This will ask a addition question and will wait for user 
        input and will validate and input. It will terurn boolean true or false
        based on if the user input is correct or wrong '''
    if (random.randrange(0,2) == 1):
        a = getRandomSingleDigitInt()
        b = getRandomSingleDigitInt()
        return additionQuestion(a,b)
    else: 
        a = getRandomSingleDigitInt()    
        b = getRandomSingleDigitIntBelow(a)
        return subtractionQuestion(a,b)


def getRandomSingleDigitInt(): #class 1
    ''' return a random single digit positive integer '''
    return random.randrange(0,10)  # this returns a single digit random number(integer). Number in python means decimal number


def getRandomSingleDigitIntBelow(x): #class 1
    ''' return a random single digit positive integer '''
    if x != 0:
        return random.randrange(0,x+1)  # this returns a single digit random number(integer). Number in python means decimal number
    else :
        return 0


def additionQuestion(a,b): #class 1
    ''' This will ask a addition question and will wait for user 
        input and will validate and input. It will terurn boolean true or false
        based on if the user input is correct or wrong '''

    print("You have "+str(TIMEOUT)+" seconds to answer this question")
    print(str(a) + " + " + str(b) + " is : ")
    ansEvent = threading.Event()
    buzzerThread = threading.Thread(name='buzzerThread', 
                    target=buzzer, args=[5, 10, ansEvent])
    buzzerThread.start()
    answerReady, _, _ = select.select([sys.stdin],[],[],TIMEOUT)
    ansEvent.set();
    # above line says that read from stdin and wait for TIMEOUT seconds 
    # If no response for TIMEOUT seconds, then retun false
    if answerReady : # if the answer has been input within the TIMEOUT seconds
        #Let us read the answer and then calculate and see if the answer is correct  
        try:
            answer = int(sys.stdin.readline().strip()) # readline() reads the answer and strip() removes the enter key
            if (answer == (a+b)): # Here we are checking if the answer is correct or wrong
                return True
            else :
                return False
        except: # If you return a non number, the code will come here
            return False
    else:
        print(" Sorry you have run out of Time to answer the question")
        return False



def subtractionQuestion(a,b): #class 1
    ''' This will ask a substraction question and will wait for user 
        input and will validate and input. It will terurn boolean true or false
        based on if the user input is correct or wrong '''

    print("You have "+str(TIMEOUT)+" seconds to answer this question")
    print(str(a) + " - " + str(b) + " is : ")
    ansEvent = threading.Event()
    buzzerThread = threading.Thread(name='buzzerThread', 
                    target=buzzer, args=[5, 10, ansEvent])
    buzzerThread.start()
    answerReady, _, _ = select.select([sys.stdin],[],[],TIMEOUT)
    ansEvent.set();
    # above line says that read from stdin and wait for TIMEOUT seconds 
    # If no response for TIMEOUT seconds, then retun false
    if answerReady : # if the answer has been input within the TIMEOUT seconds
        #Let us read the answer and then calculate and see if the answer is correct  
        try:
            answer = int(sys.stdin.readline().strip()) # readline() reads the answer and strip() removes the enter key
            if (answer == (a-b)): # Here we are checking if the answer is correct or wrong
                return True
            else :
                return False
        except: # If you return a non number, the code will come here
            return False
    else:
        print(" Sorry you have run out of Time to answer the question")
        return False
