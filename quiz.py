import sys    # this allows you to read the user input from keyboard also called "stdin"
import classOne # This imports all the classOne functions
import classTwo # This imports all the classTwo functions
import classThree # This imports all the classThree functions
import classFour # This imports all the classFour functions

TIMEOUT=10  # this is the amount of time you will wait for an answer in Seconds. 10 means 10 seconds
MAX_CLASS=5 
QUIZ_INSTRUCTIONS = """
Get ready for the quiz. You will have 10 questions out of which you 
will need 8 right to win the prize. You will have """ + str(TIMEOUT) +  """ seconds
to answer each question.Press Enter to start."""




def getUsersClass(): #main
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
    sys.stdin.readline()
    if (usersClass == 1) :
        classOne.classOneQuiz()
    elif (usersClass == 2) :
        classTwo.classTwoQuiz()
    elif(usersClass == 3):
        classThree.classThreeQuiz()
    elif(usersClass == 4):
        classFour.classFourQuiz()




