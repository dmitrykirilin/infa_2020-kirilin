from tkinter import *
from random import randrange as rnd, choice
import time
import math
root = Tk()
root.geometry('800x600')

canv = Canvas(root,bg='white')
l = Label(bg='red', fg='white', width=50, height=3, font=30)
l.pack()
canv.pack(fill=BOTH,expand=1)

scoore = 0
colors = ['red','orange','yellow','green','blue']
def new_ball():
    global x,y,r
    canv.delete(ALL)
    x = rnd(100,700)
    y = rnd(100,500)
    r = rnd(30,50)
    canv.create_oval(x-r,y-r,x+r,y+r,fill = choice(colors), width=0)
    root.after(1000,new_ball)

def click(event):
    shot = ((math.fabs(event.y - y))**2 + (math.fabs(event.x - x))**2)**0.5
    global scoore
    if shot <= r:
        scoore += 1
        l['text'] = "Goal! Scores: " + str(scoore)
        print("Goal! Scores: ", scoore)
    else:
        scoore -= 1
        l['text'] = "Fault!!! Scores: " + str(scoore)
        print("Fault!!!", scoore)

new_ball()
canv.bind('<Button-1>', click)
mainloop()