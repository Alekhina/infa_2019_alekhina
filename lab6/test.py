from tkinter import *
from random import randrange as rnd, choice
import time
root=Tk()
root.geometry('800x600')

canv=Canvas(root,bg='white')
canv.pack(fill=BOTH,expand=1)

a=canv.create_oval(20,20,100,100,fill='green')

a=canv.create_oval(300,300,500,500, fill='yellow')

mainloop()