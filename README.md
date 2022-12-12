# Wren Antivirus
<div align="center"><img src="https://raw.githubusercontent.com/Wervice/wrenav/main/EPS/Linux/media/icon.ico" width=96></div>

Wren Antivirus is going to be an open-source security all-rounder for every common os in the world. It will to support EPS, MDR and Firewalls for your IT infrastructure. Right now, it is just in the beginning. It will use ClamAV and MalwareBazaar to detect new and complicated malware fast and safe. Wren EPS also supports Live-Time-Protection and strong malware scans for Linux, MacOS and Windows. WrenAV is an open source project from Germany and has to follow the GDPR.
## How fare is it now?
+ Stable GUI for Linux
+ Virus scans for Linux
+ Live-Time for Linux
## Whats comming next?
+ Full os scanning
+ Firewall
+ File protection and backup
+ A comfortable installer
+ Managed Detection and Reaction for
+ Maybe more langauages
+ Everything also for Windows and OSX, too
## EPS
EPS is the abreviation for Endpoint Security.  
This means defend the Endpoint PC from viruses and file-loses.  
Wren EPS protects the PC using live-time watching the users home-folder, full- and systemscans, firewall and a filesafe.  
### Livetime Watching
The Livetime watching and protection uses `watchdog` to recurifly scan the users home directory. When any file changes, it will be copied to the `/tmp` directory, where ClamAV will scan it. Wren will also send a hash to MalwareBazaar to scan it for viruses. After the scan is done, Wren will remove the file from `/tmp` again.
### Scans
Wren EPS uses ClamAV and MalwareBazaar to scan file for viruses. ClamAV has modern ways to detect viruses fast and secure. MalwareBazaar has thousands of malware-hashes. This is a very safe, fast and easy way to detect new malware in sencods.
**Notice, that Wren EPS sends an HTTP Request to MalwareBazaar by [abuse.ch](https://abuse.ch). They will get your IP adress. Abuse.ch is GDPR conform and is from Switzerland. More information [here](https://wervice.github.io/wrenav/privacy).**
## MDR
MDR is the abreviation for Managed Detection and Reaction. It means, that every computer in a network gets notified when an other device was infected. So, the computer can use special tools and settings, to stop the virus infecting the network.
## Firewall
A firewall can block incomming and outgoing connections and requests. For example, it can block the port 22 for incomming requests from insecure IPs and stop attacers accessing your computers.
## Filesafe
A filesafe can protect your data against ransomeware and spyware. Ransomeware encrypts your files and wants you to pay money to get them back. Spyware steals your data and shares for example in the darkweb. The filesafe protects your by encrypting them, running the `chattr +i` command and use strong chmods like `sudo chmod 700`. It also supports backups to external drives or folders.

Wren Antivirus uses modern libraries to work. If you want to learn more about this, read [the markdown](EPS/Linux/thirdparty.md).
