###Threshhold alert for crowd analysis
from tkinter import *
import datetime
import time
import winsound

def crowdAlert():
    window = Tk()
    window.title("Alarm Clock")
    window.geometry("400x160")
    window.config(bg="#A42E14")
    window.resizable(width=False,height=False)
 
    time_format=Label(window, text= "Emergency Alert!!!", fg="white",bg="black",font=("Arial",15)).place(x=90,y=40)
    addTime = Label(window,text = "Crowd exceeds the maximum limit",font=60,fg="white",bg="black").place(x = 90, y=75)
    winsound.PlaySound("FYP/Music.wav",winsound.SND_ASYNC)
    window.mainloop()
    return  
