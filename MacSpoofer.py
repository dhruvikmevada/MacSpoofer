"""
Date Created: 12-06-2019
Developed By: Mevada Dhruvik
E-mail: dhruvikhm98@gmail.com
Description of script: MAC address spoofer script which will change the mac address of an ethernet or and wlan interface.
                       You have to input the interface name and then provide the mac address you want to change to.
Syntax ( execute this in terminal ) : python macSpoofer.py -i (interface name; e.g: wlan0) -m (mac address; e.g: 00:11:22:33:44:55)
Note: This program will only work in Linux.
Version: 1.2

"""
#!/usr/bin/env python

import subprocess
import optparse

parser = optparse.OptionParser()

parser.add_option("-i", dest="interface", help="Interface name to change it's MAC address")
parser.add_option("-m", dest="newMac", help="New MAC address")

(options, arguments) = parser.parse_args()

interface = options.interface
newMac = options.newMac

print("\n###################################################################")
print("\n[+] Changing the MAC address for " + interface + " to " + newMac)
subprocess.call(["ifconfig", interface, "down"])
subprocess.call(["ifconfig", interface, "hw", "ether", newMac])
subprocess.call(["ifconfig", interface, "up"])
print("\n[+] Done!")
print("\n###################################################################")
print("\n New MAC address : " + subprocess.call(["ifocnfig"], interface))

