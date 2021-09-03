from tkinter import *
import random
import time

def starts():
    global Score
    Score = 0
    global Enemy
    Enemy = []
    start.destroy()
    Draw()
    Player()

def Draw():
    global Score
    Score += 0.5
    var.set("Started: " + str(Score))
    global Enemy
    if random.randint(1, 100) >= 100:
        Enemy.append(enemy())
    root.after(10, movement)


def enemy():
    x = [500, 260]
    return x

def dead():
    
    global start
    start = Button(frame, text="Start", command=starts)
    start.grid(row=1,column=1)
    
    can.delete("all")
    Dead = can.create_polygon(0, 0, 0, 400, 400, 400, 400, 0, fill="red")
    return True

def Player():
    global xpos
    xpos = 20
    global ypos
    ypos = 250
    global jumpspeed
    jumpspeed = 0
    global jumps
    jumps = 0
    can.create_polygon(xpos, ypos, xpos, ypos+40, xpos+40, ypos+40, xpos+40, ypos, fill="orange")

def movement():
    global xpos
    global ypos
    global jumpspeed
    global jumps
    global Enemy
    global death
    death = False
    if jumpspeed == 1:
        if jumps < 0:
            jumps += 0.25
        elif jumps == 0:
            jumps = 0
            jumpspeed = 2
    if jumpspeed == 2:
        if ypos != 250:
            jumps += 0.25
        else:
            jumps = 0
            jumpspeed = 0
    ypos += jumps
    can.delete("all")
    for i in Enemy:
        can.create_polygon(i[0], i[1], i[0], i[1]+30, i[0]+30, i[1]+30, i[0]+30, i[1], fill="green")
        i[0] += -3

        if i[0] <= -50:
            Enemy.remove(i)
        if xpos  <= i[0] + 30 and xpos + 40 >= i[0] and ypos <= i[1] + 30 and ypos + 40 >= i[1]:
            death = dead()
            break
    if death != True:
        can.create_polygon(xpos, ypos, xpos, ypos+40, xpos+40, ypos+40, xpos+40, ypos, fill="orange")
        Draw()

def Jump(event):
    global jumpspeed
    global jumps
    if jumpspeed == 0:
        jumps = -7
        jumpspeed = 1

root = Tk()
can = Canvas(root, width=400, height=400)
can.pack(side=TOP)

var = StringVar()
global Textlines
Textlines = Label(root, textvariable=var, relief=RAISED)
Textlines.pack()


frame = Frame(root)
frame.place(relx = 0.5, rely = 0.5, anchor = "center")

start = Button(frame, text="Start", command=starts)
start.grid(row=1,column=1)

root.bind("<space>", Jump)

can.pack()

root.mainloop()
