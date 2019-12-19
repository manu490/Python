import urllib.request,urllib.parse,urllib.error
import json
serviceurl='http://py4e-data.dr-chuck.net/geojson?'
while True:
    address=input('Enter the location : ')
    if (len(address)<1):break
    url=serviceurl + urllib.parse.urlencode({'address':address})
    print("Retrieving data",url)
    uh=urllib.request.urlopen(url)
    data=uh.read().decode()
    print('Retrieving',len(data),'characters')
    try:
        js=json.loads(data)
    except:
        js=none

    if not js or 'status' not in js or js['status']!='OK':
        print("==Failure to Retrieve===")
        print(data)
        continue
    location=js["results"][0]["place_id"]
    print(location)
