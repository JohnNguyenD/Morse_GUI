from tkinter import *
import tkinter.font
from gpiozero import LED
import RPi.GPIO
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18,GPIO.OUT)
RPi.GPIO.setmode(RPi.GPIO.BCM)

win = Tk()
win.title("Morse Code")
myFont = tkinter.font.Font(family = 'Helvetica', size = 12, weight = "bold")
win.configure(background = "tan")


left = Label(win, text = "Insert Text")
left.grid(row = 0, column =0)

right = Entry(win,bd =3)
right.grid(row = 0, column =1)

Conversion = {"a":".-",
              "b": "-...",
              "c": "-.-.",
              "d": "-..",
              "e": ".",
              "f": "..-.",
              "g": "--.",
              "h": "....",
              "i": "..",
              "j": ".---",
              "k": "-.-",
              "l": ".-..",
              "m": "--",
              "n": "-.",
              "o": "---",
              "p": ".--.",
              "q": "--.-",
              "r": ".-.",
              "s": "...",
              "t": "-",
              "u": "..-",
              "v": "...-",
              "w": ".--",
              "x": "-..-",
              "y": "-.--",
              "z": "--..",}
## define Dot and Dash
def Dot():
    GPIO.output(18,GPIO.HIGH)
    time.sleep(0.25)
    GPIO.output(18,GPIO.LOW)
    time.sleep(0.25)

def Dash():
    GPIO.output(18,GPIO.HIGH)
    time.sleep(1)
    GPIO.output(18,GPIO.LOW)
    time.sleep(1)

def export():
    text = right.get().lower()
    if len(text) > 12:
        print("Out of range")
        Close()
    for i in range(len(text)):
        blink = Conversion[text[i]]
        
        for z in range(len(blink)):
            char = blink[z]
            if char == '.':
                Dot()
            elif char == '-':
                Dash()
        time.sleep(3)

def Close():
    win.destroy()
    exit()

exportButton = Button(win, text = 'Export', command = export, bg = "snow")
exportButton.grid(row =1, column =1)

exitButton = Button(win, text = 'Exit', command = Close, bg = "red")
exitButton.grid(row = 2,column =1)




        
