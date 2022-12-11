import time
import clamd
import shutil
import hashlib
import requests
import json
import os
from pathlib import Path
from modules import wrenbox
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler
from termcolor import colored
clam = clamd.ClamdUnixSocket()
def clamscan(file):
    try:
        id = hashlib.sha256(open(file, "rb").read()).hexdigest()
        shutil.copy(file, "/tmp/wrenscanfile__"+id)
        scan = clam.scan("/tmp/wrenscanfile__"+id)
        os.remove("/tmp/wrenscanfile__"+id)
        restring = [str(scan[str("/tmp/wrenscanfile__"+id)][0]), str(scan[str("/tmp/wrenscanfile__"+id)][1])]
    except FileNotFoundError:
        restring = ["ERROR", "FileNotFoundError"]
    return restring
def malwarebazaar(file):
    try:
        id = hashlib.sha256(open(file, "rb").read()).hexdigest()
        r = requests.post(url="https://mb-api.abuse.ch/api/v1/", data={
                "query":"get_info",
                "hash":str(id)
            })
        restring = json.loads(r.text)["query_status"]
    except FileNotFoundError:
        restring = ""
    return restring
def virus_found_f(malware, file):
            wrenbox.warning(subtitle="The scan found a virus.", title="Virus found", detail="Wren EPS Linux Edition found malware in "+file+".\n("+malware+")")
            # reaction.cry(malware=malware)
class Event(LoggingEventHandler):
    def on_created(self, event):
        print("Scanning...")
        if event.is_directory == False:
            path = event.src_path
            clamavscan = clamscan(path)
            mbzaarscan = malwarebazaar(path)
            clamavscan_bolean = (clamavscan[0] == 'OK') == False
            mbzaarscan_bolean = (mbzaarscan == 'file_not_found') == True
            if mbzaarscan_bolean and clamavscan[0] != "ERROR":
                virus_found_f(clamavscan[1], path)
            elif clamavscan_bolean and clamavscan[0] != "ERROR" and clamavscan[0] != "":
                virus_found_f(clamavscan[1], path)
    def on_modified(self, event):
        print("Scanning...")
        if event.is_directory == False:
            path = event.src_path
            clamavscan = clamscan(path)
            mbzaarscan = malwarebazaar(path)
            clamavscan_bolean = (clamavscan[0] == 'OK') == False
            mbzaarscan_bolean = (mbzaarscan == 'file_not_found') == True
            if mbzaarscan_bolean and clamavscan[0] != "ERROR":
                virus_found_f(clamavscan[1], path)
            elif clamavscan_bolean and clamavscan[0] != "ERROR" and clamavscan[0] != "":
                virus_found_f(clamavscan[1], path)
path = str(Path.home())
event_handler = Event()
observer = Observer()
observer.schedule(event_handler, path, recursive=True)
observer.start()
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()
observer.join()