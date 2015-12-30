import random # This allows you to generate random numbers
import select # This allows you to wait for a specific time for input from user
import sys    # this allows you to read the user input from keyboard also called "stdin"

TIMEOUT=10  # this is the amount of time you will wait for an answer in Seconds. 10 means 10 seconds
QUESTION_COUNT=10
ANSWER_GOAL=8


def classFourQuiz(): # Class 4
    '''this will the Quiz for CLASS 4'''
    questionCount = 0
    correctAnswers = 0
    while(questionCount < QUESTION_COUNT):
        if (additionQuestionClassFour()) :
            correctAnswers = correctAnswers + 1;
        questionCount = questionCount + 1
    print("You got " + str(correctAnswers) + " correct");
    if(correctAnswers >= ANSWER_GOAL):
        print("congratulations!,you win!!!")
    else :
        print("sorry,better luck next time:)")
          




def additionQuestionClassFour(): #class 4
    ''' This will ask a addition question and will wait for user 
        input and will validate and input. It will terurn boolean true or false
        based on if the user input is correct or wrong '''
    if (random.randrange(0,2) == 1):
        a = getRandomTripleDigitInt()
        b = getRandomDoubleSingleDigitInt()
        return additionQuestion(a,b)
    else: 
        a = getRandomTripleDigitInt()    
        b = getRandomDoubleSingleDigitInt()
        return subtractionQuestion(a,b)

def getRandomDoubleSingleDigitInt(): #class 4
    ''' return a random single digit positive integer '''
    return random.randrange(0,100)  # this returns a single digit random number(integer). Number in python means decimal number


def getRandomTripleDigitInt(): #class 4
    ''' return a random single digit positive integer '''
    return random.randrange(100,500)  # this returns a single digit random number(integer). Number in python means decimal number


def getRandomDoubleSingleDigitIntBelow(x): #class 4
    ''' return a random single digit positive integer '''
    if x != 0:
        return random.randrange(0,x+1)  # this returns a single digit random number(integer). Number in python means decimal number
    else :
        return 0


def additionQuestion(a,b): #class 4
    ''' This will ask a addition question and will wait for user 
        input and will validate and input. It will terurn boolean true or false
        based on if the user input is correct or wrong '''

    print("You have "+str(TIMEOUT)+" seconds to answer this question")
    print(str(a) + " + " + str(b) + " is : ")
    answerReady, _, _ = select.select([sys.stdin],[],[],TIMEOUT)
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



def subtractionQuestion(a,b): #class 4
    ''' This will ask a substraction question and will wait for user 
        input and will validate and input. It will terurn boolean true or false
        based on if the user input is correct or wrong '''

    print("You have "+str(TIMEOUT)+" seconds to answer this question")
    print(str(a) + " - " + str(b) + " is : ")
    answerReady, _, _ = select.select([sys.stdin],[],[],TIMEOUT)
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
