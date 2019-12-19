import urllib.request,urllib.parse,urllib.error
import json
address=input('Enter the location : ')
url=address
print("Retrieving data",url)
data=urllib.request.urlopen(url).read()
print('Retrieving',len(data),'characters')
js=json.loads(data)
js=js["comments"]
sum=0
for item in js:
    count=int(item["count"])
    print("count:",count)
    sum=sum+count
print("sum:",sum)
