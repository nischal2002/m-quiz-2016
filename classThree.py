import random # This allows you to generate random numbers

import os # This module is used to check if we are running on pi
import quizEngine

if (os.uname().nodename == 'raspberrypi'):
    from ledControl import greenLedOn
    from ledControl import redLedOn
    from ledControl import redLedBuzzerOn
else:
    from ledControlNoop import greenLedOn
    from ledControlNoop import redLedOn
    from ledControlNoop import redLedBuzzerOn



TIMEOUT=10  # this is the amount of time you will wait for an answer in Seconds. 10 means 10 seconds
QUESTION_COUNT=10
ANSWER_GOAL=8
LED_ON_TIME=2
BETTER_LUCK_TIME=3

          
def classThreeQuiz(): # Class 1
    '''this will the Quiz for CLASS 1'''
    questionCount = 0
    correctAnswers = 0
    while(questionCount < QUESTION_COUNT):
        questionTxt, answer = getQuestionClassThree()
        if(quizEngine.runQuestion(questionTxt, answer, TIMEOUT)):
            greenLedOn(LED_ON_TIME)
            correctAnswers = correctAnswers + 1
        else:
            redLedBuzzerOn(LED_ON_TIME)
        questionCount = questionCount + 1
    print("You got " + str(correctAnswers) + " correct");
    if(correctAnswers >= ANSWER_GOAL):
        print("congratulations!,you win!!!")
        greenLedOn(BETTER_LUCK_TIME)
    else:
        print("sorry,better luck next time:)")
        redLedBuzzerOn(BETTER_LUCK_TIME)

def getQuestionClassThree():
    ''' This will ask a addition question and will wait for user 
        input and will validate and input. It will terurn boolean true or false
        based on if the user input is correct or wrong '''
    if (random.randrange(0,2) == 1):
        a = getRandomDoubleSingleDigitInt()
        b = getRandomDoubleSingleDigitInt()
        qText = "You have "+str(TIMEOUT)+" seconds to answer this question\n"
        qText += str(a) + " + " + str(b) + " is : "
        return (qText,(a+b))
    else: 
        a = getRandomDoubleSingleDigitInt()    
        b = getRandomDoubleSingleDigitIntBelow(a)
        qText = "You have "+str(TIMEOUT)+" seconds to answer this question\n"
        qText += str(a) + " - " + str(b) + " is : "
        return (qText,(a-b))
    

def getRandomDoubleSingleDigitInt(): #class 3
    ''' return a random single digit positive integer '''
    return random.randrange(0,100)  # this returns a single digit random number(integer). Number in python means decimal number


def getRandomTripleDigitInt(): #class 3
    ''' return a random single digit positive integer '''
    return random.randrange(100,500)  # this returns a single digit random number(integer). Number in python means decimal number


def getRandomDoubleSingleDigitIntBelow(x): #class 3
    ''' return a random single digit positive integer '''
    if x != 0:
        return random.randrange(0,x+1)  # this returns a single digit random number(integer). Number in python means decimal number
    else :
        return 0
