from itertools import combinations_with_replacement
def product(lst):
  mulp=1
  for i in lst:
    mulp*=i
  return mulp
N,K=map(int,input().split())
itgrs=list(map(int,input().split()))
x=product(itgrs)
st=set()
count=0
for i in range(1,x+1):
  if x%i == 0:
    st.add(i)
subs=set(combinations_with_replacement(sorted(st), K))
#print(subs)
for i in subs:
  mult=1
  for element in i:
    mult*=element
  if mult==x:
    #print(i)
    count+=1
print(count)
