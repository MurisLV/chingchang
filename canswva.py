from email.mime import image
import gc
import getopt
from tkinter import *


canvas_width = 600 
canvas_height = 600

master = Tk()
x1=300
y1=300
x2=150
y2=250
e=5
f='blue'
teksts=30
g=100
g=100
biezums=5
def clicked(event):
    print("pressed")
    e=30
w = Canvas(master, 
           width=canvas_width, 
           height=canvas_height)






w.pack()

def uzaugsu():
    global x1, y1, x2, y2, e, f, c, player
    x2=x1+0
    y2=y1-10
    c = w.create_line(x1, y1, x2, y2, width=e, fill=f )
    player =w.create_rectangle(x2,y2)
    x1=x2
    y1=y2
    print(x1)
    print(y1)
    while gc>0:
           k = input('virziens')
    if k=='w':
        uzaugsu()
        g=getopt-1
        biezums()




w.create_text(50,560,text='atslēga: ')
w.create_rectangle(540,500, 10, 10)
buttonBG = w.create_rectangle(160, 550, 220, 575, fill="white", outline="grey60")
buttonTXT = w.create_text(179, 560, text= 'Time: ')
buttonBG = w.create_rectangle(79, 550, 100, 575, fill="red", outline="grey60")
buttonTXT = w.create_text(90, 560, text= 'y/n')



w.pack



mainloop()