from logging import info
from tkinter import*
from tkinter import ttk
from matplotlib.figure import Figure
from Function import function1

import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import os

global darkmode
global figureBackgroudColor

backgroudColor = "#313233"
figureBackgroudColor="#313233"
labelColor = 'white'
buttonColor = '#9E7141'
plotColor = '#9E7141'
plotStyle = 'line'
darkmode = True

number_list = []

moreThanOne = False
numberOfAddedPlots = 0

#Clears the entry of any inputs.

def clearTextInput():
    e.delete(0, 'end')

def clearTree():
    for i in numberTree.get_children():
        numberTree.delete(i)

def basicInformationUpdate():
    global numberOfAddedPlots
    try:
        numberOfAddedPlots = 0
        input = int(e.get())
        if input > 0:
            clearTree()
            global number_list
            number_list.clear()

            inputs.set('Your input: ' + e.get())
            number_list = function1(int(e.get()))
            s = len(number_list)
            highestNumber = int(max(number_list))
            steps.set('Steps taken: ' + str(s))
            maxNumber.set('Highest value: ' + str(highestNumber))
            #Filling treeview of the list of numbers.

            for i,j in zip(range(s), number_list):
                numberTree.insert(parent='',index='end',values=(i+1,j))
            clearCanvas()
        else:
            inputs.set('Input must be an positive integer')
    except:
        inputs.set('Input must be an positive integer')


def plot():
    a.clear()

    x = list(range(1,len(number_list)+1))
    y = number_list

    a.tick_params(top=False, axis='x', colors='white')
    a.tick_params(right=False, axis='y', colors='white')
    a.xaxis.label.set_color('white')
    a.yaxis.label.set_color('white')

    if plotStyle == 'Line & Dot':
        a.scatter(x,y, color = plotColor, s=10)
        a.plot(x,y, color = plotColor)
    elif plotStyle == 'Dot':
        a.scatter(x,y, color = plotColor, s=10)
    elif plotStyle == 'Bar':
        a.bar(x,y, color=plotColor)
    else:
        a.plot(x,y, plotColor)

    canvas.draw()

def restartGUI():
    root.destroy()
    os.startfile('Collatz Conjecture GUI.pyw')
    

def clearCanvas():
    a.clear()

#Get values from combobox and update plot accordingly
def plotUpdate():
    global plotColor
    global plotStyle
    
    if numberOfAddedPlots == 0:
        if plotColorDrop.get() in plotColors:
            plotColor = plotColorDrop.get()
        if plotColorDrop.get() == 'Default':
            plotColor = '#9E7141'
        else:
            plotColor = plotColorDrop.get()

        plotStyle = plotStyleDrop.get()

        plot()
    else:
        pass

def addPlot():
    global numberOfAddedPlots
    global moreThanOne
    if moreThanOne == False:
        addColor = 'red'
        moreThanOne=True
        numberOfAddedPlots += 1 
    else:
        numberOfAddedPlots += 1 
        numberOfAddedPlots = numberOfAddedPlots%12
        moreThanOne=True
        colors = ['Black', "Gray", "Silver", "Purple", "Green", "Lime", "Olive", "Yellow", "Navy", "Blue", "Teal", "Aqua"]
        addColor=colors[numberOfAddedPlots]

    global number_list
    number_list.clear()
    number_list = function1(int(e.get()))
    x = list(range(1,len(number_list)+1))
    y = number_list

    if plotStyle == 'Line & Dot':
        a.scatter(x,y, color = addColor, s=10)
        a.plot(x,y, color = addColor)
    elif plotStyle == 'Dot':
        a.scatter(x,y, color = addColor, s=10)
    elif plotStyle == 'Bar':
        a.bar(x,y, color=addColor)
    else:
        a.plot(x,y, addColor)

    canvas.draw()

def darkModeBG():
    optionsMenu.delete('Dark Mode')
    optionsMenu.add_command(label='Light Mode', command=lightModeBG)
    backgroudColor = "#313233"
    buttonColor = '#9E7141'
    f.set_facecolor(backgroudColor)
    canvas.draw()
    root.config(bg=backgroudColor)
    submitButton.configure(bg=buttonColor)
    addPlotButton.configure(bg=buttonColor)
    plotUpdateButton.configure(bg=buttonColor)

    stepsLabel.config(bg=backgroudColor, fg='white')
    inputsLabel.config(bg=backgroudColor, fg='white')
    maxNumberLabel.config(bg=backgroudColor, fg='white')
    plotColorLabel.config(bg=backgroudColor, fg='white')
    plotStyleLabel.config(bg=backgroudColor, fg='white')


def lightModeBG():
    optionsMenu.delete('Light Mode')
    optionsMenu.add_command(label='Dark Mode', command=darkModeBG)

    buttonColor='gray'
    backgroudColor = 'white'
    f.set_facecolor(backgroudColor)
    canvas.draw()
    root.config(bg='white')
    submitButton.configure(bg=buttonColor)
    addPlotButton.configure(bg=buttonColor)
    plotUpdateButton.configure(bg=buttonColor)

    stepsLabel.config(bg=backgroudColor, fg='black')
    inputsLabel.config(bg=backgroudColor, fg='black')
    maxNumberLabel.config(bg=backgroudColor, fg='black')
    plotColorLabel.config(bg=backgroudColor, fg='black')
    plotStyleLabel.config(bg=backgroudColor, fg='black')

    



root = Tk()
root.geometry('620x510')
root.title('Collatz conjecture')


#Entry to get user inputs

e=Entry(root, width=30)
e.insert(0, "Enter an positive integer: ", )
e.grid(row=0, column=0, padx=10, pady=5,ipady=3)




root.configure(background=backgroudColor)


#input variables

inputs = StringVar()
steps = StringVar()
lists = StringVar()
maxNumber = StringVar()

#Set default values so they're visible from the start.

inputs.set('Your input was: ')
steps.set('Steps taken: ')
maxNumber.set('Highest value: ')


#all the labels

inputsLabel = Label(root, textvariable=inputs, background=backgroudColor, width=26, anchor=W, padx=10, fg='white', pady=3)
stepsLabel = Label(root, textvariable=steps, background=backgroudColor, width=26, anchor=W, padx=10, fg='white',pady=3)
maxNumberLabel = Label(root, textvariable=maxNumber, background=backgroudColor, width=26, anchor=W, padx=10, fg='white',pady=3)
# Grid all labels
inputsLabel.grid(row=1, column=0, sticky=W)
stepsLabel.grid(row=2, column=0, sticky=W)
maxNumberLabel.grid(row=3, column=0, sticky=W)


#Figure and canvas for plotting charts

f = Figure(figsize=(4,4), dpi=100)
a = f.add_subplot(111)
canvas = FigureCanvasTkAgg(f, root)

f.set_facecolor(figureBackgroudColor)
a.set_facecolor("#ffffff")
a.plot(0,0)
a.tick_params(top=False, axis='x', colors='white')
a.tick_params(right=False, axis='y', colors='white')

canvas.draw()
canvas.get_tk_widget().grid(row=5, column=2)


#Buttons
submitButton = Button(root, text='Input',fg='white', height=1, width=5, bg=buttonColor, command= lambda:[basicInformationUpdate(), plot(), clearTextInput()])
plotUpdateButton = Button(root, text='Update',fg='white', background=buttonColor,height=1, width=5, command= plotUpdate)
addPlotButton = Button(root, text='Add', fg='white', bg=buttonColor,height=1, width=5, command=lambda:[addPlot(), clearTextInput()])

submitButton.grid(row=0, column=1)
plotUpdateButton.grid(row=2, column=1, pady=5)
addPlotButton.grid(row=1, column=1)

#Treeview - to display list of all numbers
numberTree = ttk.Treeview(root)

numberTree['columns'] = ('Step', 'Value')
numberTree.column('#0', width=0, minwidth=0)
numberTree.column("Step", anchor=CENTER, width=91, minwidth=91)
numberTree.column("Value", anchor=CENTER, width=91, minwidth=91)

numberTree.heading('Step', text="Step (x-axis)", anchor=CENTER)
numberTree.heading('Value', text="Value (y-axis)", anchor=CENTER)

numberTree.grid(row=5, column=0, stick=N, pady=48)

#Values for drop downs
plotColors = ['Default', 'Black', "White", "Gray", "Silver", "Red", "Purple", "Green", "Lime", "Olive", "Yellow", "Navy", "Blue", "Teal", "Aqua"]
plotStyles = ['Line','Bar', 'Dot', 'Line & Dot']
    
#Drop downs for plot customisation

plotColorDrop = ttk.Combobox(root, values=plotColors)
plotStyleDrop = ttk.Combobox(root, values=plotStyles)

plotColorDrop.grid(row=2, column=2, sticky=E, padx=40)
plotStyleDrop.grid(row=2, column=2, sticky=W, padx=50)

plotColorDrop.current(0)
plotStyleDrop.current(0)

#Labels above dropdown boxes.
plotStyleLabel = Label(root, text="Plot styles", background=backgroudColor, fg='white')

plotColorLabel = Label(root, text="Plot colors", background=backgroudColor, fg='white')

plotStyleLabel.grid(row=1, column=2, sticky=W, padx=90)
plotColorLabel.grid(row=1, column=2, sticky=E, padx=80)

#Options menu

guiMenu = Menu(root)
root.config(menu=guiMenu)

optionsMenu = Menu(guiMenu)

guiMenu.add_cascade(label = "Options", menu=optionsMenu)

optionsMenu.add_command(label='Light Mode', command=lightModeBG)


#Power menu
powerMenu = Menu(guiMenu)

guiMenu.add_cascade(label = 'Power' , menu=powerMenu)

powerMenu.add_command(label='Restart', command=restartGUI)
powerMenu.add_command(label='Exit', command=root.quit)

#Options menu to change colors
fileInfoFrame = Frame(root, width=620, height=510, bg='red')

#Main loop that keeps gui functioning
root.mainloop()
