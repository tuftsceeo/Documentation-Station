#!/usr/bin/python
#!/bin/bash
import Tkinter as tk
import os
"""SetDateTime.py: GUI that uses buttons to set the date and time of the raspberry pi"""
__author__ = "Fiona Chung"

#TO FIX:
    #-if the user inputs 10 incorrect digits (ex. 9999999999), what happens?
    #-idea for future: make MMDDYY input easier by having separate entry boxes or different windows
    #-make prettier :)

#sets up the GUI        
root = tk.Tk()
root.title('Set Time and Date.   Version 2.0')

#Makes GUI correct size and places in middle of screen
w = 430 #window width
h = 430 #window height
#get screen info
ws = root.winfo_screenwidth()
hs = root.winfo_screenheight()
#calculate coordinates for window
x=(ws-w)/2
y=(hs-h)/2
#set dimension of screen and location
root.geometry('%dx%d+%d+%d' % (w,h,x,y))

def clear():
    """Clears everything"""
    display.delete(0,tk.END)
    
def get_variables(num):
    """Gets input and puts it in box"""
    global i
    display.insert(i,num)
    i += 1

def undo():
    """Deletes last entered number from box"""
    updated_string = display.get()[:-1]
    clear()
    display.insert(0,updated_string)
    
def submit():
    """Updates time and date on raspberry pi, closes GUI, and runs documentation station program.
    If the user did not enter 10 digits, directions are highlighted in red"""
    if len(display.get())!=10:
        directions.config(fg="red")
    else:
        date = display.get()
        command = "sudo date " + date
        os.system(command) #sets date on the raspberry pi
        root.quit() #closes GUI
        os.system('sudo python /home/pi/docstation_2.0.py') #runs doc station program
        
# creates a label to display directions for user  
directions = tk.Label(root, font=("Courier",14), text="Enter month, day, hour, minute, year\nin the format: MMDDhhmmYY\n(Hours are in military time)")
directions.grid(row=0,column=0,columnspan=10)

# creates entry box for user to enter date and time        
display = tk.Entry(root, font=("Courier",30))
display.grid(row=1,column=0,columnspan=16)

# makes a list of buttons (numbers 0-9)
buttons =[]
for i in range(0,10):
    button = tk.Button(root,text=str(i),command=lambda num=i: get_variables(num),height=1,width=5,font=("Courier",20))
    buttons.append(button)

# adds all of the buttons to the panel
# this part of the code is a lil inefficient so numbers on display appear like on a traditional calculator
# adds buttons 7-9 to panel
c=1
for i in range(7,10):
    buttons[i].grid(row=2,column=c,sticky="NWSE")
    c+=1
# adds buttons 4-6 to panel
c=1
for i in range(4,7):
    buttons[i].grid(row=3,column=c,sticky="NWSE")
    c+=1    
# adds buttons 1-3 to panel
c=1
for i in range(1,4):
    buttons[i].grid(row=4,column=c,sticky="NWSE")
    c+=1  
# adds button 0 to panel
buttons[0].grid(row=5,column=1,columnspan=2,sticky="NWSE")

# makes undo button and adds to panel  
undo = tk.Button(root,text="<-",command=undo)
undo.grid(row=5,column=3,sticky="NWSE")

# makes clear button and adds to panel   
cls = tk.Button(root,text="Clear",command=clear,font=("Courier",20))
cls.grid(row=7,column=1,columnspan=1,sticky="NWSE")   

# makes submit button and adds to panel
submit = tk.Button(root,text="Submit",command=submit,font=("Courier",20))
submit.grid(row=7,column=2,columnspan=2,sticky="NWSE")
 
root.mainloop()
