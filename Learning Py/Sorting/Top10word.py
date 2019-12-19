fhand=open('short.txt')
counts=dict()
for line in fhand:
    words=line.split()
    for word in words:
        counts[word]=counts.get(word,0)+1
lst=list()
for k,v in counts.items():
    newtap=(v,k)
    lst.append(newtap)
lst=sorted(lst,reverse=True)
for v,k in lst[:10]:
    print(k,v)
