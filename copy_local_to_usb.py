#!/usr/bin/python
import os
import Tkinter as tk


#Checks if the USB is inserted by checking if there is a folder named USBDRV in the /media/pi
#if no USBDRV folder found if prints error
#makes the directory if it does not exists and then copies the files

#to make it better, adjust code so the if statement is not necessary
#(should be possible!)


#The below code prints a window to confirm that the copy was done succesfully
top= tk.Tk()

#Makes GUI correct size and places in middle of screen
w = 430 #window width
h = 107 #window height
#get screen info
ws = top.winfo_screenwidth()
hs = top.winfo_screenheight()
#calculate coordinates for window
x=(ws-w)/2
y=(hs-h)/2
#set dimension of screen and location
top.geometry('%dx%d+%d+%d' % (w,h,x,y))

def close():
    """it will close the pop up window"""
    top.quit()


#if USBDRV folder found
if os.path.exists("/media/pi/USBDRV"):
    if not os.path.exists("/media/pi/USBDRV/Local_to_USB/"):
        os.makedirs("/media/pi/USBDRV/Local_to_USB")
    #if you want to see what is being copied (in command terminal), edit the line below to say 'sudo cp -vr...'
    os.system('sudo cp -r /home/pi/Photos/* /media/pi/USBDRV/Local_to_USB')

    
    top.title('Success')
    label= tk.Label(top, text= "Your files have successfully copied", font=("Courier",14))
    label.pack()
    button= tk.Button(top,text="Ok", font=("Courier",14),command=close)
    button.pack()
    top.mainloop()
#if USBDRV folder not found
else:
    top.title('Error')
    label= tk.Label(top, text= "No USB device found", font=("Courier",14))
    label.pack()
    button= tk.Button(top,text="Ok", font=("Courier",14),command=close)
    button.pack()
    top.mainloop()
    
    
