#we will import the tkinter to make a gui
from tkinter import *
from tkinter import ttk

#it is better to define the functions at the start so that it is easy to find
#these functions take in one number
def percent():
    CurrentValue = float(CurrentResult.get())
    CurrentResult.set(str(CurrentValue / 100))
def divideoneby():
    CurrentValue = float(CurrentResult.get())
    CurrentResult.set(str(1 / CurrentValue))
def squared():
    CurrentValue = float(CurrentResult.get())
    CurrentResult.set(str(CurrentValue**2))
def squareroot():
    CurrentValue = float(CurrentResult.get())
    CurrentResult.set(str(CurrentValue**(1/2)))
def negate():
    CurrentValue = float(CurrentResult.get())
    CurrentResult.set(str(CurrentValue*(-1)))

#by making num1 global, the results of this function persist outside of the function; we set the operation based on what button the user selected
def divide():
    global num1
    num1 = float(CurrentResult.get())
    Operation.set("/")
    CurrentResult.set("")
def multiply():
    global num1
    num1 = float(CurrentResult.get())
    Operation.set("*")
    CurrentResult.set("")
def add():
    global num1
    num1 = float(CurrentResult.get())
    Operation.set("+")
    CurrentResult.set("")
def subtract():
    global num1
    num1 = float(CurrentResult.get())
    Operation.set("-")
    CurrentResult.set("")

#the calculate function will use the second number in addition to the global num1
def calculate():
    num2 = float(CurrentResult.get())
    op = Operation.get()
    #this performs the mathematical Operation based off of what the person clicked earlier and what the Operation was set as in the previous function
    if op == "+":
        result = num1 + num2
    elif op == "-":
        result = num1 - num2
    elif op == "*":
        result = num1 * num2
    elif op == "/":
        result = num1 / num2
    #this uses an f string to print the equation in the previous result area
    PreviousResult.set(f"{num1} {op} {num2} =")
    #this prints the result of the calculation in the current result area
    CurrentResult.set(str(result))

#this concatenates all the inputs together as a string to display in the calculator's display
def click(value):
    CurrentValue = CurrentResult.get()
    CurrentResult.set(CurrentValue+str(value))
#this is the function to clear the inputs
def clear():
    CurrentResult.set("")
    PreviousResult.set("")

#this will create the main window for our gui
CalcGui = Tk()

#this will give the window a name
CalcGui.title("Basic Calculator")

#this will set the color of the window
CalcGui.config(bg="#474747")

#this creates the frame that will hold the calculator buttons and display
CalcFrame = ttk.Frame(CalcGui, padding="4 8 5 5")
#this defines the grid and the directions we will use for stying our calculator buttons and display
CalcFrame.grid(column=0, row=0, sticky=(N, W, E, S))
#CalcGui.columnconfigure(0, weight=1)
#CalcGui.rowconfigure(0, weight=1)

#initialize the StringVar variables
CurrentResult = StringVar()
PreviousResult = StringVar()
Operation = StringVar()

#this is the calculators display port that displays the result of the previous and current calculation
PreviousRes= ttk.Label(CalcFrame, textvariable=PreviousResult).grid(column=4, row=1, columnspan=4, sticky=E)
CurrentRes = ttk.Label(CalcFrame, textvariable=CurrentResult).grid(column=4, row=2, columnspan=4, sticky=E)

# this creates the first column of the calculator
ttk.Button(CalcFrame, text="%", command=percent).grid(column=1, row=3, sticky=E)
ttk.Button(CalcFrame, text="1/x", command=divideoneby).grid(column=1, row=4, sticky=E)
ttk.Button(CalcFrame, text="7", command=lambda: click(7)).grid(column=1, row=5, sticky=E)
ttk.Button(CalcFrame, text="4", command=lambda: click(4)).grid(column=1, row=6, sticky=E)
ttk.Button(CalcFrame, text="1", command=lambda: click(1)).grid(column=1, row=7, sticky=E)
ttk.Button(CalcFrame, text="+/-", command=negate).grid(column=1, row=8, sticky=E)

# this creates the second column of the calculator
ttk.Button(CalcFrame, text="CE", command=clear).grid(column=2, row=3, sticky=E)
ttk.Button(CalcFrame, text="x^2", command=squared).grid(column=2, row=4, sticky=E)
ttk.Button(CalcFrame, text="8", command=lambda: click(8)).grid(column=2, row=5, sticky=E)
ttk.Button(CalcFrame, text="5", command=lambda: click(5)).grid(column=2, row=6, sticky=E)
ttk.Button(CalcFrame, text="2", command=lambda: click(2)).grid(column=2, row=7, sticky=E)
ttk.Button(CalcFrame, text="0", command=lambda: click(0)).grid(column=2, row=8, sticky=E)

# this creates the third column of the calculator
ttk.Button(CalcFrame, text="C", command=clear).grid(column=3, row=3, sticky=E)
ttk.Button(CalcFrame, text="x^1/2", command=squareroot).grid(column=3, row=4, sticky=E)
ttk.Button(CalcFrame, text="9", command=lambda: click(9)).grid(column=3, row=5, sticky=E)
ttk.Button(CalcFrame, text="6", command=lambda: click(6)).grid(column=3, row=6, sticky=E)
ttk.Button(CalcFrame, text="3", command=lambda: click(3)).grid(column=3, row=7, sticky=E)
ttk.Button(CalcFrame, text=".", command=lambda: click(".")).grid(column=3, row=8, sticky=E)

# this creates the last column that contains the main operators and the calculate button
ttk.Button(CalcFrame, text="Backspace").grid(column=4, row=3, sticky=W)
ttk.Button(CalcFrame, text="Divide", command=divide).grid(column=4, row=4, sticky=W)
ttk.Button(CalcFrame, text="Multiply", command=multiply).grid(column=4, row=5, sticky=W)
ttk.Button(CalcFrame, text="Subtract", command=subtract).grid(column=4, row=6, sticky=W)
ttk.Button(CalcFrame, text="Add", command=add).grid(column=4, row=7, sticky=W)
ttk.Button(CalcFrame, text="Calculate", command=calculate).grid(column=4, row=8, sticky=W)

#this will run the application/open the window
CalcGui.mainloop()
