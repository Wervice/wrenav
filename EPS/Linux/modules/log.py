from termcolor import colored
from datetime import datetime

file = open("log.log", "a")
def info(message):
    now = datetime.now()
    print(colored("INFO | "+now.strftime("%d/%m/%Y %H:%M:%S")+" | "+message, "blue"))
    file.write("\n"+"INFO | "+now.strftime("%d/%m/%Y %H:%M:%S")+" | "+message)
def warn(message):
    now = datetime.now()
    print(colored("WARN | "+now.strftime("%d/%m/%Y %H:%M:%S")+" | "+message, "yellow"))
    file.write("\n"+"WARN | "+now.strftime("%d/%m/%Y %H:%M:%S")+" | "+message)
def fail(message):
    now = datetime.now()
    print(colored("FAIL | "+now.strftime("%d/%m/%Y %H:%M:%S")+" | "+message, "red"))
    file.write("\n"+"FAIL | "+now.strftime("%d/%m/%Y %H:%M:%S")+" | "+message)
def done(message):
    now = datetime.now()
    print(colored("DONE | "+now.strftime("%d/%m/%Y %H:%M:%S")+" | "+message, "green"))
    file.write("\n"+"DONE | "+now.strftime("%d/%m/%Y %H:%M:%S")+" | "+message)