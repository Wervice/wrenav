from tkinter import *
def new(master, text, color, foreground, font, winwidth):
    Label(master=master,text=" "+text, font=font, background=color, foreground=foreground, width=winwidth, height=2, anchor="w").place(x=0,y=0)