from tkinter import *
from tkinter.ttk import *
from ttkthemes import ThemedTk, ThemedStyle
def error(subtitle, title, detail, font = "Ubuntu", multiple = False, buttonb = None):
    window = ThemedTk(theme="arc")
    window.title(title)
    window.resizable(False, False)
    window.geometry("400x300+200+200")
    window.configure(background = "white")
    Label(master=window,text="\n "+title+"\n", font=(font, 17, "bold"), background = "#e39714", foreground="white", width=400).place(x=0,y=0)
    Message(master=window, text=subtitle, font=(font, 10), width=390, background="white").place(x=0, y=90)
    Message(master=window, text=detail, font=(font, 12), width=390, background="white").place(x=0, y=115)
    Button(master=window, text="Got it", command=window.destroy).place(x=275, y=250)
    window.mainloop()

def info(subtitle, title, detail, multiple = False, buttonb = None):
    window = ThemedTk(theme="arc")
    window.title(title)
    window.resizable(False, False)
    window.geometry("400x300+200+200")
    window.configure(background = "white")
    Label(master=window,text="\n "+title+"\n", font=("Ubuntu", 17, "bold"), background = "#246de3", foreground="white", width=400).place(x=0,y=0)
    Message(master=window, text=subtitle, font=("Ubuntu", 10), width=390, background="white").place(x=0, y=90)
    Message(master=window, text=detail, font=("Ubuntu", 12), width=390, background="white").place(x=0, y=115)
    Button(master=window, text="Got it", command=window.destroy).place(x=275, y=250)
    window.mainloop()

def success(subtitle, title, detail, multiple = False, buttonb = None):
    window = ThemedTk(theme="arc")
    window.title(title)
    window.resizable(False, False)
    window.geometry("400x300+200+200")
    window.configure(background = "white")
    Label(master=window,text="\n "+title+"\n", font=("Ubuntu", 17, "bold"), background = "#3aa115", foreground="white", width=400).place(x=0,y=0)
    Message(master=window, text=subtitle, font=("Ubuntu", 10), width=390, background="white").place(x=0, y=90)
    Message(master=window, text=detail, font=("Ubuntu", 12), width=390, background="white").place(x=0, y=115)
    Button(master=window, text="Got it", command=window.destroy).place(x=275, y=250)
    window.mainloop()

def warning(subtitle, title, detail, multiple = False, buttonb = None):
    window = ThemedTk(theme="arc")
    window.title(title)
    window.resizable(False, False)
    window.geometry("400x300+200+200")
    window.configure(background = "white")
    Label(master=window,text="\n "+title+"\n", font=("Ubuntu", 17, "bold"), background = "#e33424", foreground="white", width=400).place(x=0,y=0)
    Message(master=window, text=subtitle, font=("Ubuntu", 10), width=390, background="white").place(x=0, y=90)
    Message(master=window, text=detail, font=("Ubuntu", 12), width=390, background="white").place(x=0, y=115)
    Button(master=window, text="Got it", command=window.destroy).place(x=275, y=250)
    window.mainloop()