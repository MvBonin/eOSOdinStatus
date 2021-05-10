#!/usr/bin/python3
import urllib.request
from bs4 import BeautifulSoup
#from notify import notification
import sys
import os
from pydbus import SessionBus

os.environ['DBUS_SESSION_BUS_ADDRESS'] = 'unix:path=/run/user/'+ str(os.geteuid()) +'/bus'
os.environ['DISPLAY'] = ':0'

bus = SessionBus()
notifications = bus.get('.Notifications')




## Is the Notification arg set? -n
isNotificationArg = False
if len(sys.argv) > 1:
    if sys.argv[1] == "-n":
        isNotificationArg = True


content = urllib.request.urlopen('https://github.com/orgs/elementary/projects/55')

read_content = content.read()

soup = BeautifulSoup(read_content, 'html.parser')

tooltip = soup.find(class_ = "tooltipped tooltipped-s")
lastUpdated = soup.find("relative-time", class_ = "no-wrap")
sendString =  tooltip['aria-label'] + " - Updated " + lastUpdated.text
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
    notifications.Notify('test', 0, 'computer', "eOS 6.0 Odin Dev Status", sendString, [], {}, 5000)
    with open(".lastStatus", "w") as f:
        f.write(sendString)
print(sendString)



##to debug use runner.sh -n > /home/USER/tmp.fetch 2>&1 in crontab