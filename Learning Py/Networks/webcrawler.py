
import urllib.request, urllib.parse, urllib.error
from urllib.request import Request, urlopen
import ssl
from bs4 import BeautifulSoup
#ssl error ignoring
ctx=ssl.create_default_context()
ctx.check_hostname=False
ctx.verify_mode=ssl.CERT_NONE
url = input('Enter - ')
count=0
ct=int(input('count:'))
pos=int(input('position:'))
#print(url)
while count<ct:
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    html = urllib.request.urlopen(req).read()
    soup = BeautifulSoup(html, 'html.parser')
    # Retrieve all of the anchor tags
    tags = soup('a')
    position=0
    for tag in tags:
        #print(tag.get('href', None))
        position=position+1
        if position==pos:
            break
    url=tag.get('href', None)
    name=tag.contents[0]
    count=count+1
    #print('Retrieving',url)
print(name)
