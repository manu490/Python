import socket
from bs4 import BeautifulSoup
import ssl
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('192.168.43.3', 80))


while True:
    cmd = 'GET http://192.168.43.3 HTTP/1.0\r\n\r\n'.encode()
    mysock.send(cmd)
    data = mysock.recv(512)
    if (len(data) < 1):
        break
    html=data.decode()
    soup=BeautifulSoup(html,'html.parser')
    tags=soup('p')
    for tag in tags:
      # print ('TAG:',tag) #lists all span tags
      #print ('Contents:',tag.contents[0]) #lists content of tag span!!
      # print ('Attrs:',tag.attrs) #checks tag attributes like class...
       value=tag.contents[0]
    print(value)
