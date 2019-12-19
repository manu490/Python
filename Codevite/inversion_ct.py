n=int(input())
intgrs=tuple(map(int,input().split(',')))
seq=[]
count=0
for each in intgrs:
  ones=bin(each).count("1")
  seq.append(ones)
for i in range(len(seq)):
  for j in range(i+1,len(seq)):
    if seq[i]>seq[j]:
      count+=1
print(count)
