# Wren EPS Linux Edition
<div align="center"><image src="media/icon.ico" width=96></div>

## What is Wren EPS Linux Edition
Wren EPS is the Endpoint Security Software for Linux by Wren by Wervice. It's written in Python. The latest release is Hunting Hamster Beta.
Wren EPS Linux Edition uses third-party libraries. Please have a look [here](thirdparty.md), if you want to learn more about them.
## Meaning and using of files
### `Dashboard.py`
This is the main file. It contains code for scanning for viruses and the GUI. It also starts the Watchfile script.
CHMOD: sudo, +rx, -w
CHATTR: sudo, +i
### `Watchfile.py`
This is the file watching script. It watches the home folder for new files, and automaticly scans them for viruses. This is an esntial tool to protect the user.  
CHMOD: sudo, +rx, -w  
CHATTR: sudo, +i  
### `mdrhost`
This is a file to store the variable mdrhost. The installer has to init it. It tells the Watchfile and Dashboard, where the MDR Host is.  
CHMOD: sudo, +r,-wx  
CHATRR: sudo, +i  
### `lastscan`
This variable stores, when was the last full or system scan.  
CHMOD: +rw, -x
### `lastupdate`
This variable stores, when was the last cvdupdate.  
CHMOD: +rw, -x
### `pcid`
This variable stores the MDR PC Name. It's inited by the installer.
CHMOD: sudo, +r, -wx
CHATTR: sudo, +i
### `uthread`
This variable stores a boolean. It checks, is there an unhandled threat or the device is in emergency mode.
CHMOD +rw, -x
### `eicar`
This is the EICAR Test file.
CHMOD: +rw, -x
### `log.log`
This is the scan log.
CHMOD: +rw, -x
### `log.py`
This python script logs information while debugging and working.
### `modules>topbar.py`
This python script creats colored top bars in Tkitner windows
### `modules>wrenbox.py`
This python script creates good looking Tkinter message boxes.
### `media>icon.ico`
This image is the Wren EPS Linux logo
<br><br>

> by [Wervice](https.//wervice.github.io)