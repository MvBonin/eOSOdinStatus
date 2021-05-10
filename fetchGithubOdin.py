import urllib.request
from bs4 import BeautifulSoup

content = urllib.request.urlopen('https://github.com/orgs/elementary/projects/55')

read_content = content.read()

soup = BeautifulSoup(read_content, 'html.parser')

tooltip = soup.find(class_ = "tooltipped tooltipped-s")
if tooltip:
    print(tooltip['aria-label'])
