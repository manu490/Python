name=input('Enter file: ')
handle=open(name)
counts=dict()
for line in handle:
    words=line.split()
    for word in words:
        counts[word]=counts.get(word,0)+1

Bigcount= -1
Bigword= None
for word,count in counts.items():
    if count>Bigcount:
        Bigword=word
        Bigcount=count
print(Bigcount,Bigword)
