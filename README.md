# MacSpoofer

This python script will allow a user to spoof it's system's MAC address.

Syntax (will only work in linux os): #python macSpoofer -i (interface name; e.g: eth0 or wlan0) -m (new MAC address eg: 00:11:22:3a:45:66)

To get back the original MAC address type the following command in linux terminal

#ethtool -P (your interface name)
