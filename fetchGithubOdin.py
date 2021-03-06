#!/usr/bin/python3
import urllib.request
from bs4 import BeautifulSoup
#from notify import notification
import sys
import os
import argparse

from pydbus import SessionBus

os.environ['DBUS_SESSION_BUS_ADDRESS'] = 'unix:path=/run/user/'+ str(os.geteuid()) +'/bus'
os.environ['DISPLAY'] = ':0'

bus = SessionBus()
notifications = bus.get('.Notifications')

## Is the Notification arg set? -n
parser = argparse.ArgumentParser(description="Check elementaryOS Odin Status from github")
parser.add_argument("--notify", "-n", action="store_true", help="Show Notification, even it it didn't change since last time you checked")
args = parser.parse_args()

isNotificationArg = args.notify


content = urllib.request.urlopen('https://github.com/orgs/elementary/projects/90') ##CHANGE URL HERE FOR DIFFERENT GITHUB PROJECT

read_content = content.read()

soup = BeautifulSoup(read_content, 'html.parser')

tooltip = soup.find(class_ = "tooltipped tooltipped-s")
lastUpdated = soup.find("relative-time", class_ = "no-wrap")
ttiparia = tooltip['aria-label']

if ttiparia == "0 done / 0 in progress / 0 to do":
    sendString =  "Updated " + lastUpdated.text
else:
    sendString =  ttiparia + " - Updated " + lastUpdated.text
lastRead = ""

try:
    f = open(".lastStatus", "r")
except IOError:
    print("not openable")
    g = open(".lastStatus", "x")
    g.write(sendString)
    isNotificationArg = True
    g.close()


with open(".lastStatus", "r") as f:
    lastRead = f.read()


if lastRead != sendString or isNotificationArg:
    print("Status Notification")
    #notification(sendString, title='eOS 6.0 Odin Dev Status', app_name="elementaryOS", image="computer")
    notifications.Notify('test', 0, 'computer', "eOS 6.1 Odin Dev Status", sendString, [], {}, 5000)
    with open(".lastStatus", "w") as f:
        f.write(sendString)
print(sendString)



##to debug use runner.sh -n > /home/USER/tmp.fetch 2>&1 in crontab