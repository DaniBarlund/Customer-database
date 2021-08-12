import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
#steps has to be counted outside the function because the recursion will always change the amount of steps taken back to 0
steps = 0
#numberlist is a global variable that contains all the numbers that the function will give.
numberlist = []

#Get users input on what number he wants to run the function on.
#userInput=int(input('Enter a number: '))

# Define the 3x+1 function and use it's recursion to count the amount of steps taken to get in the 4-1 loop.
def function1(number):
    #global keyword is needed because the variable steps is modified inside the function.
    global steps
    global numberlist
    if number==1:
        return numberlist
    elif number%2==0:
        number = number / 2
        numberlist.append(int(number))
        return function1(number)
    else:
        number = number*3+1
        numberlist.append(int(number))
        return function1(number)

#function1(number)
#print('steps taken to get to number 1 was: ' + str(steps))
#print(numberlist)

