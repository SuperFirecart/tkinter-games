from tkinter import *
import random
import time

global Square

def starts():
    global milliseconds1
    global Failure
    Failure = 3
    global Score
    Score = 0
    milliseconds1 = int(round(time.time()*1000))
    frame.destroy()
    start.destroy()
    square()

def square():
    global Square
    global Failure
    global var
    if Failure == 0:
        can.delete("all")
        Dead = can.create_polygon(0, 0, 0, 400, 400, 400, 400, 0, fill="red")
        global frame
        frame = Frame(root)
        frame.place(relx = 0.5, rely = 0.5, anchor = "center")
        global start
        start = Button(frame, text="Start", command=starts)
        start.grid(row=1,column=1)
        var.set("Score: " + str(Score) + "\nLives: " + str(Failure))
    else:
        global milliseconds1
        milliseconds1 = int(round(time.time()*1000))
        can.delete("all") 
        xpos = random.randint(1, 380)
        ypos = random.randint(1, 380)
        Square = can.create_polygon(xpos, ypos, xpos, ypos+40, xpos+40, ypos+40, xpos+40, ypos, fill="orange")
        can.tag_bind(Square, "<Button-1>", within_square)
        var.set("Score: " + str(Score) + "\nLives: " + str(Failure))
       


def within_square(event):
    global Score
    global Failure
    global milliseconds2
    milliseconds2 = int(round(time.time()*1000))
    if milliseconds2 - milliseconds1 >= 2000:
        Failure -= 1
        square()
    else:
        Score += 1
        square()

def movement():
    Square.xpos += 1
    
root = Tk()

can = Canvas(root, width=400, height=400)
can.pack(side=TOP)

var = StringVar()
global Textlines
Textlines = Label(root, textvariable=var, relief=RAISED)

frame = Frame(root)
frame.place(relx = 0.5, rely = 0.5, anchor = "center")

start = Button(frame, text="Start", command=starts)
start.grid(row=1,column=1)


can.pack()

Textlines.pack()
root.mainloop()
