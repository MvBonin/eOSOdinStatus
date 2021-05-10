import urllib.request
from bs4 import BeautifulSoup
from notify import notification

content = urllib.request.urlopen('https://github.com/orgs/elementary/projects/55')

read_content = content.read()

soup = BeautifulSoup(read_content, 'html.parser')

tooltip = soup.find(class_ = "tooltipped tooltipped-s")
lastUpdated = soup.find("relative-time", class_ = "no-wrap")
if tooltip:
    
    sendString =  tooltip['aria-label'] + " - Updated " + lastUpdated.text
    print(sendString)
    notification(sendString, title='eOS Odin Dev Status')
