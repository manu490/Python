import urllib.request,urllib.parse,urllib.error
from bs4 import BeautifulSoup
import ssl
#ssl error ignoring
#ctx=ssl.create_default_context()
#ctx.check_hostname=False
#ctx.verify_mode=ssl.CERT_NONE

url=input('Enter URL: ')
html=urllib.request.urlopen(url).read() #html=urllib.request.urlopen(url,context=ctx).read()
soup=BeautifulSoup(html,'html.parser')
tags=soup('span')
sum=0
for tag in tags:
  # print ('TAG:',tag) #lists all span tags
  #print ('Contents:',tag.contents[0]) #lists content of tag span!!
  # print ('Attrs:',tag.attrs) #checks tag attributes like class...
   value=int(tag.contents[0])
   sum=sum+ value
print("total number of comments",sum)
