import random # This allows you to generate random numbers
import select # This allows you to wait for a specific time for input from user
import sys    # this allows you to read the user input from keyboard also called "stdin"


TIMEOUT=10  # this is the amount of time you will wait for an answer in Seconds. 10 means 10 seconds
MAX_CLASS=5 
QUIZ_INSTRUCTIONS = """
Get ready for the quiz. You will have 10 questions out of which you 
will need 8 right to win the prize. You will have """ + str(TIMEOUT) +  """ seconds
to answer each question"""

def getRandomSingleDigitInt():
    ''' return a random single digit positive integer '''
    return random.randrange(0,9)  # this returns a single digit random number(integer). Number in python means decimal number


def getRandomSingleDigitIntBelow(x):
    ''' return a random single digit positive integer '''
    if x != 0:
        return random.randrange(0,x)  # this returns a single digit random number(integer). Number in python means decimal number
    else :
        return 0

def additionQuestion(a,b):
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



def subtractionQuestion(a,b):
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

def getUsersClass():
    ''' This function will get the user's class. It will compare the class with MAX_CLASS and
    will return False if it is more than the MAX_CLASS. Class also has to be a natural number ''' 
    print("Please tell me which Class you are in? ")
    try:
        usersClass = int(sys.stdin.readline().strip())
        if (usersClass < 1 or usersClass > MAX_CLASS) :
            print("No Quiz available for Class " + str(usersClass))
            return False
        else :
            return usersClass
    except :
        print("Exception")
        return False


if __name__ == '__main__':
    while(True) :
        usersClass = getUsersClass()
        if (usersClass != False) :
            break

    print(QUIZ_INSTRUCTIONS)




