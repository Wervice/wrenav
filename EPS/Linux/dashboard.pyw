from tkinter import *
from tkinter import filedialog
import tkinter as tk
from tkinter.ttk import *
from ttkthemes import ThemedTk, ThemedStyle
from termcolor import colored
from modules import wrenbox, topbar, log
from subprocess import Popen
from PIL import Image, ImageTk
import hashlib
import shutil
import clamd
import os
import requests
import json
import sys
# sudo apt install clamav-cvdupdate

# Check OS. If it's not linux, a message will appear.
"""if sys.platform != "linux" and sys.platform != "linux2":
    wrenbox.error("You're not running Linux", title="Wrong Editon", detail="You're trying to run Wren Endpoint Security Linux Edition under Win32 or OSX. This application won't work correctly under Windows or OSX. Please download the correct edition for your OS.", font="sans-serif")
    exit()"""

clam = clamd.ClamdUnixSocket()
def scromve(path):
    i = 0
    size = os.stat(path).st_size
    string = ""
    while i != size:
        string = string+"?"
        i = i+1
    open(path, "w").write(string)
    os.remove(path)
def clamscan(file):
    try:    
        id = hashlib.sha256(open(file, "rb").read()).hexdigest()
        shutil.copy(file, "/tmp/wrenscanfile__"+id)
        scan = clam.scan("/tmp/wrenscanfile__"+id)
    except PermissionError:
        print(colored("You've no permissions to access this file or folder.", "red"))
        wrenbox.error(subtitle="You can't access this resource.", title="Permission Error", detail="To access this file or folder you need permssions, you don't have. Try to restart the application with root or sudo permisions, to fix this error.")
    return [str(scan[str("/tmp/wrenscanfile__"+id)][0]), str(scan[str("/tmp/wrenscanfile__"+id)][1])]
def malwarebazaar(file):
    try:
        id = hashlib.sha256(open(file, "rb").read()).hexdigest()
        r = requests.post(url="https://mb-api.abuse.ch/api/v1/", data={
                "query":"get_info",
                "hash":str(id)
            })
    except PermissionError:
        print(colored("You've no permissions to access this file or folder.", "red"))
        wrenbox.error(subtitle="You can't access this resource.", title="Permission Error", detail="To access this file or folder you need permssions, you don't have. Try to restart the application with root or sudo permisions, to fix this error.")
    return json.loads(r.text)["query_status"]
def main():
    def m_scan():
        window.destroy()
        def scn_file():
            log.info("Starting file scan now")
            def virus_found_f(malware = "Unknown", file=""):
                def remove():
                    os.remove(file)
                    wrenbox.info("File removed", title="File remove", detail="The virus is removed from your hard drive. You can close this window and the warning window now.")
                wrenbox.warning(subtitle="The scan found a virus.", title="Virus found", detail="The file you scanned contains code of a virus.\n("+malware+")", multiple=True, buttonbdesc="Remove", buttonbcmd=remove)
            def no_virus_found_f():
                wrenbox.info(subtitle="The scan found no virus.", title="No virus found", detail="The file you scanned contains no virus.\nIt's not found on MalwareBazaar or ClamAV.")
            path = filedialog.askopenfilename()
            clamavscan = clamscan(path)
            mbzaarscan = malwarebazaar(path)
            clamavscan_bolean = (clamavscan[0] == 'OK') == False
            mbzaarscan_bolean = (mbzaarscan == 'file_not_found') == True
            if clamavscan_bolean and mbzaarscan_bolean:
                virus_found_f(malware=clamavscan[1], file=path)
            elif clamavscan_bolean:
                virus_found_f(malware=clamavscan[1], file=path)
            elif mbzaarscan_bolean:
                virus_found_f(file=path)
            else:
                no_virus_found_f()
        def scn_folder():
            log.info("Starting folder scan now")
            def virus_found_f(malware = "Unknown", file=[""]):
                def remove():
                    for file in file:
                        os.remove(file)
                        wrenbox.info("File removed", title="File remove", detail="The virus is removed from your hard drive. You can close this window and the warning window now.")
                wrenbox.warning(subtitle="The scan found viruses.", title="Virus found", detail="The files you scanned, contain malware.\n"+malware, multiple=True, buttonbdesc="Remove", buttonbcmd=remove)
            def no_virus_found_f():
                wrenbox.info(subtitle="The scan found no virus.", title="No virus found", detail="The folder you scanned contains no virus.")
            dirname = filedialog.askdirectory()
            viruses = ""
            viruses_array = []
            for root, dirs, files in os.walk(dirname):
                for file in files:
                    file_path = os.path.join(root, file)
                    clamscanres = clamscan(file_path)
                    mbzaarscanres = malwarebazaar(file_path)
                    if clamscanres[0] == "OK" and mbzaarscanres == "hash_not_found":
                        pass
                    else:
                        viruses = viruses+"\n"+file+" ("+clamscanres[1]+")"
                        viruses_array += [file_path]
            if viruses != "":
                virus_found_f(malware=viruses, file=viruses_array)
            else:
                no_virus_found_f()
        def scn_system():
            log.info("Scanning system folders (bin;etc;var;lib;sys;usr;run)")
            def virus_found_f(malware = "Unknown", file=[""]):
                def remove():
                    for file in file:
                        os.remove(file)
                        wrenbox.info("File removed", title="File remove", detail="The virus is removed from your hard drive. You can close this window and the warning window now.")
                wrenbox.warning(subtitle="The scan found viruses.", title="Virus found", detail="The files you scanned, contain malware.\n"+malware, multiple=True, buttonbdesc="Remove", buttonbcmd=remove)
            def no_virus_found_f():
                wrenbox.info(subtitle="The scan found no virus.", title="No virus found", detail="The system you scanned contains no virus.")
            def scn(dir):
                dirname = dir
                viruses = ""
                viruses_array = [""]
                for root, dirs, files in os.walk(dirname):
                    for file in files:
                        file_path = os.path.join(root, file)
                        clamscanres = clamscan(file_path)
                        mbzaarscanres = malwarebazaar(file_path)
                        if clamscanres[0] == "OK" and mbzaarscanres == "hash_not_found":
                            pass
                        else:
                            viruses = viruses+"\n"+file+" ("+clamscanres[1]+")"
                            viruses_array += [file_path]
                if viruses != "":
                    virus_found_f(malware=viruses, file=viruses_array)
                else:
                    pass
                return viruses_array
            # Scan for viruses in theese directories...
            a = scn("/bin")
            b = scn("/etc")
            c = scn("/var")
            d = scn("/lib")
            e = scn("/sys")
            f = scn("/usr")
            g = scn("/run")
            if a == [""] and b == [""] and c == [""] and d == [""] and e == [""] and f == [""] and g == [""]:
                no_virus_found_f()
        def scn_full():
            log.info("Scanning whole system")
            def virus_found_f(malware = "Unknown", file=[""]):
                def remove():
                    for file in file:
                        os.remove(file)
                        wrenbox.info("File removed", title="File remove", detail="The virus is removed from your hard drive. You can close this window and the warning window now.")
                wrenbox.warning(subtitle="The scan found viruses.", title="Virus found", detail="The files you scanned, contain malware.\n"+malware, multiple=True, buttonbdesc="Remove", buttonbcmd=remove)
            def no_virus_found_f():
                wrenbox.info(subtitle="The scan found no virus.", title="No virus found", detail="The system you scanned contains no virus.")
            def scn(dir):
                dirname = dir
                viruses = ""
                viruses_array = [""]
                for root, dirs, files in os.walk(dirname):
                    for file in files:
                        file_path = os.path.join(root, file)
                        clamscanres = clamscan(file_path)
                        mbzaarscanres = malwarebazaar(file_path)
                        if clamscanres[0] == "OK" and mbzaarscanres == "hash_not_found":
                            pass
                        else:
                            viruses = viruses+"\n"+file+" ("+clamscanres[1]+")"
                            viruses_array += [file_path]
                if viruses != "":
                    virus_found_f(malware=viruses, file=viruses_array)
                else:
                    pass
                return viruses_array
            # Scan for viruses in theese directories...
            a = scn("/")
            if a == [""]:
                no_virus_found_f()
        def scn_fdis():
            pass
        scan_window = ThemedTk(theme="arc")
        scan_window.title("Wren Antivirus - Virus Scan")
        scan_window.geometry("600x285+100+100")
        scan_window.configure(background = "white")
        scan_window.wm_resizable(False, False)
        topbar.new(master=scan_window, text="Malware Scan", color="#2175eb", foreground="white", font=("Ubuntu", 15, "bold"), winwidth=600)
        Label(master=scan_window, text="Scan a single file for viruses.", font=('Ubuntu', 12), background="white").place(x=160, y=65)
        Label(master=scan_window, text="Scan a single folder for viruses.", font=('Ubuntu', 12), background="white").place(x=160, y=110)
        Label(master=scan_window, text="Scan the system and packages.", font=('Ubuntu', 12), background="white").place(x=160, y=155)
        Label(master=scan_window, text="Scan all your files for viruses.", font=('Ubuntu', 12), background="white").place(x=160, y=200)
        Label(master=scan_window, text="Autoremove all viruses from this system, when found.", font=('Ubuntu', 12), background="white").place(x=160, y=245)
        Button(master=scan_window, width=12, text="Scan File", command=scn_file).place(x=10, y=60)
        Button(master=scan_window, width=12, text="Scan Folder", command=scn_folder).place(x=10, y=105)
        Button(master=scan_window, width=12, text="Scan System", command=scn_system).place(x=10, y=150)
        Button(master=scan_window, width=12, text="Full Scan", command=scn_full).place(x=10, y=195)
        Button(master=scan_window, width=12, text="Full Desinfect", command=scn_fdis).place(x=10, y=240)
    def m_fsafe():
        pass
    def m_firewall():
        pass
    def m_cleanup():
        pass
    def m_settings():
        pass
    def update_main():
        log.info("Updating virus definitions using CVDUpdate")
        os.system("cvdupdate update")
        open("lastupdate", "w").write(str(now*10000000))
        window.destroy()
        os.system("python3 dashboard.pyw")
        log.done("Virus definitions update done")
    window = ThemedTk(theme="arc")
    window.title("Wren Antivirus Endpoint Security")
    window.geometry("600x285+100+100")
    window.wm_resizable(False, False)
    window.configure(background = "white")
    ico = Image.open('./media/icon.ico')
    photo = ImageTk.PhotoImage(ico)
    window.wm_iconphoto(True, photo)
    topbar.new(master=window, text="Wren Antivirus", color="#2175eb", foreground="white", font=("Ubuntu", 15, "bold"), winwidth=75)
    Button(text="Scans", width=12, command=m_scan).place(x=10, y=60)
    Button(text="File Safe", width=12, command=m_fsafe).place(x=10, y=105)
    Button(text="Firewall", width=12, command=m_firewall).place(x=10, y=150)
    Button(text="Cleanup", width=12, command=m_cleanup).place(x=10, y=195)
    Button(text="Settings", width=12, command=m_settings).place(x=10, y=240)
    tk.Frame(master=window, background="#ededed", width=410, height=200).place(x=160, y=65)
    from datetime import datetime
    date= datetime.utcnow() - datetime(1970, 1, 1)
    seconds =(date.total_seconds())
    milliseconds = round(seconds*1000)
    now = milliseconds
    lastupdate = int(open("lastupdate", "r").read())
    lastscan = int(open("lastscan", "r").read())
    unhandled_threat = bool(open("uthreat", "r").read())
    if now > lastupdate + 3600000:
        statusbar = tk.Frame(master=window, background="#e33424", width=410, height=30).place(x=160, y=65)
        statuslabel = tk.Label(master=window, background="#e33424", height=1, foreground="white", text="Old virus definitions", font=("Ubuntu", 12, "bold")).place(x=165, y=67.5)
        statusmessage = tk.Message(master=window, background="#ededed", foreground="black", text="Please update your virus definitions. They are important for scanning files or folder for viruses. If they are old, newer viruses may be not found. A update takes up to 5 minutes. After that, Wren will restart.", width=400).place(x=165, y=100)
        button_update = Button(master=window, text="Update now", command=update_main).place(x=175, y=220)
    elif now > lastscan + 86400000:
        statusbar = tk.Frame(master=window, background="#e33424", width=410, height=30).place(x=160, y=65)
        statuslabel = tk.Label(master=window, background="#e33424", height=1, foreground="white", text="Old scan", font=("Ubuntu", 12, "bold")).place(x=165, y=67.5)
        statusmessage = tk.Message(master=window, background="#ededed", foreground="black", text="The last scan is older then one day. Please start a new system or full scan to check, that there are no new malware on your system. Often, you don't see that you're infected, without a scan.", width=400).place(x=165, y=100)
    elif unhandled_threat:
        statusbar = tk.Frame(master=window, background="#e33424", width=410, height=30).place(x=160, y=65)
        statuslabel = tk.Label(master=window, background="#e33424", height=1, foreground="white", text="Unhandled threat", font=("Ubuntu", 12, "bold")).place(x=165, y=67.5)
        statusmessage = tk.Message(master=window, background="#ededed", foreground="black", text="A virus scan found a virus. You haven't decided what shout happen to the virus. You can remove it or keep it on your drive.", width=400).place(x=165, y=100)
    else:
        statusbar = tk.Frame(master=window, background="#3aa115", width=410, height=30).place(x=160, y=65)
        statuslabel = tk.Label(master=window, background="#e33424", height=1, foreground="white", text="All caught up", font=("Ubuntu", 12, "bold")).place(x=165, y=67.5)
        statusmessage = tk.Message(master=window, background="#ededed", foreground="black", text="Everything is ok.", width=400).place(x=165, y=100)
    window.mainloop()
cwd = os.getcwd()
p = Popen(['watch', "python3 watchfile.py"])
main()