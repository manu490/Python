import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

url = 'http://py4e-data.dr-chuck.net/comments_42.xml'

url = input('Enter location: ')
print('Retrieving', url)
data = urllib.request.urlopen(url).read()
print('Retrieved', len(data), 'characters')
#print(data.decode())
tree = ET.fromstring(data)

results = tree.findall('comments/comment')
print('Retrieved', len(results), 'characters')
sum=0
for item in results:
    #print('count', item.find('count').text)
    sum+=int(item.find('count').text)
print(sum)
