from itertools import combinations
arr=list(map(int,input().split(',')))
def rem(lst):
  for x in lst:
    while x in arr:
      arr.remove(x)
for i in arr:
  for j in arr:
    if(int(str(i)+str(j))<24):
      hrs=[str(i),str(j)]
rem(hrs)
for i in arr:
  for j in arr:
    if(int(str(i)+str(j))<60):
      mins=[str(i),str(j)]
rem(mins)
for i in arr:
  for j in arr:
    if(int(str(i)+str(j))<60):
      secs=[str(i),str(j)]
print(''.join(hrs),''.join(mins),''.join(secs),sep=':')
