import math
from math import cos, asin, sqrt
def distance(lat1, lon1, lat2, lon2):
    s = math.pi/180
    a = 0.5-cos((lat2-lat1)*s)/2+cos(lat1*s)*cos(lat2*s)*(1-cos((lon2 - lon1)*s))/2 #Formula from Internet
    return 6400*2*asin(sqrt(a))
n = int(input())
ords=[]
totaldistance=0
for i in range(n):
  ords.append(str(input()))

for i in range(len(ords)-1):
  ls,lo=ords[i].split(',')
  ls1,lo1=ords[i+1].split(',')
  if 'N' in ls:
    lat=int(ls.replace('N',''))
  if 'E' in lo:
    lon=int(lo.replace('E',''))
  if 'S' in ls:
    lat=-int(ls.replace('S',''))
  if 'W' in lo:
    lon=-int(lo.replace('W',''))
  if 'N' in ls1:
    lat1=int(ls1.replace('N',''))
  if 'E' in lo1:
    lon1=int(lo1.replace('E',''))
  if 'S' in ls1:
    lat1=-int(ls1.replace('S',''))
  if 'W' in lo1:
    lon1=-int(lo1.replace('W',''))
  totaldistance+=distance(lat,lon,lat1,lon1)
print(int(round(totaldistance)))
