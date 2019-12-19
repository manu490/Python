import urllib.request,urllib.parse,urllib.error

fhand=urllib.request.urlopen('http://py4e-data.dr-chuck.net/comments_7892.html')
counts=dict()
for line in fhand:
    words=line.decode().strip()
    print(words)
    #print('words:',words)
    #print('counting')
    #for word in words:
        ##print(counts)
