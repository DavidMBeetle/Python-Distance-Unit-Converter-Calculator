#Copyright © 2026–Present DavidMBeetle. GNU General Public License v3.0

#importing libraries
import tkinter as GUI
import math

#global variables:

global OutputUnit1

global OutputUnit2

global conversionValueInt

Output = 0
#this will be necessary for converting the list box input into a given one

#creating custom functions

def ClearWindow():
    label.destroy()
    conversionValue.destroy()
    inputtedUnit.destroy()
    ConvertButton.destroy()


def DisplayOutput(InputVar1, InputVar2, Unit1, Unit2):
    
    #Adding them to the scope like so
    OutputUnit1 = GUI.Label(Window, text=f"{InputVar1:.2f} " + f"{Unit1}")
    OutputUnit2 = GUI.Label(Window, text=f"{InputVar2:.2f} " + f"{Unit2}")

    OutputLabel = GUI.Label(Window, text="Outputted conversions:")
    OutputLabel.place(x=150, y=100)
    OutputUnit1.place(x=150, y=120)
    OutputUnit2.place(x=150, y=140)



def convert():
    #checking if inputted conversion value is okay
    conversionValueInput = conversionValue.get()
    


    print(conversionValueInput)
    #verifying that conversion value is valid
    if (conversionValueInput.isdigit() == True):
        print('Value is Valid!')
        #doing converts
        #before doing converts we need to verify that the units are not the same
        
        #Just giving it a random value since it will be replaced anyway
        
        InputSelection = inputtedUnit.curselection()
        print(InputSelection)
        conversionValueInput = int(conversionValueInput)
        if (InputSelection[0] == 0):
            print('Kilometer selected')
            ClearWindow()
            conversionValueInput = int(conversionValueInput)
            convertedUnit1 = conversionValueInput * 0.621371
            convertedUnit2 = conversionValueInput * 1000
            DisplayOutput(convertedUnit1, convertedUnit2, 'Mile(s)', 'Meter(s)')

        elif (InputSelection[0] == 1):
            print("Miles selected")
            ClearWindow()
            conversionValueInput = int(conversionValueInput)
            convertedUnit1 = conversionValueInput * 1.60934
            convertedUnit2 = conversionValueInput * 1609.34
            DisplayOutput(convertedUnit1, convertedUnit2, 'Kilometer(s)', 'Meter(s)')
        elif (InputSelection[0] == 2):
            print("Meters selected")
            ClearWindow()
            conversionValueInput = int(conversionValueInput)
            convertedUnit1 = conversionValueInput / 1609.34
            convertedUnit2 = conversionValueInput / 1000
            DisplayOutput(convertedUnit1, convertedUnit2, 'Mile(s)', 'Kilometer(s)')

    print(inputtedUnit.curselection())

#Create main window
Window = GUI.Tk()

#set title

Window.title("Distance Unit converter")

#Set size

Window.geometry("500x500")

#Adding Label

label = GUI.Label(Window, text="Input # of units")
label.place(x=110, y=40)

#Creating list of supported Units

supported_Units = ["Kilometers (km)", "Miles (mi)", "Meters (m)"]

inputtedUnit = GUI.Listbox(Window)

for i in range(len(supported_Units)):
    inputtedUnit.insert(i, supported_Units[i])

inputtedUnit.place(x=100, y=100)


conversionValue = GUI.Entry(Window, background='grey')
conversionValue.place(x=200, y=300)

###Button for converter

ConvertButton = GUI.Button(Window, text="convert", command=convert)
ConvertButton.place(x=200, y=350)
#Drop down for units

#Start GUI event thing
Window.mainloop()

# Copyright © 2026–Present DavidMBeetle. GNU General Public License v3.0
