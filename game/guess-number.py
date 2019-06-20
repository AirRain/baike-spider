import tkinter as tk
import random
number = random.randint(0,1024)
running = True
num = 0
nmaxn = 1024
nminn = 0

def eBtnClose(event):
    root.destroy()
def eBtnGuess(event):
    global nmaxn
    global nminn
    global num
    global running
    if running:
        val_a = int(entry_a.get())
        if val_a == number:
            labelqval("答对了")
            num += 1
            running = False
            numGuess()
        elif val_a < number:
            
        

