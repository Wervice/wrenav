# Installation Guide
To use Wren EPS Linux Edition on your system, you have to follow these easy steps. If you've got questions, maybe the [FAQ](#faq) will help you. You can also write an [email to me](mailto:wervice@proton.me).
## 1. Requiriments
Please run thees commands to install all required python libraries with pip.
```
pip install tkinter
pip install pillow
pip install requests
pip install clamd
pip install watchdog
pip install ttkthemes
pip install termcolor
pip install pathlib
```
Now, you have to install Tkinter for your system. Please choose the right command for your os and run it. This may need the sudo password.
### Apt
```
sudo apt install python-tk
```
### Pacman
```
pacman -S tk
```
### Zypper
```
zypper in python-tk
```
## 2. Download
Clone the respository from github.
```
git clone https://github.com/Wervice/wrenav.git
```
## 3. Install
Now go to EPS/Linux.  
Next step is, to open up a terminal.
Run this command in the terminal:
```
python3 install.py
```
## 4. Follow the installer
Now, the installer will tell you everything and guide you to the end.