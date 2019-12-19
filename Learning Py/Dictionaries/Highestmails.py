name=input('Enter file: ')#file name is short.txt
handle=open(name)
counts=dict()
for line in handle:
    line=line.rstrip()
    if line.startswith('From:'):
        words=line.split()
        mail=words[1]
        address=mail.split()
        for word in address:
            counts[word]=counts.get(word,0)+1

Bigcount= -1
Bigword= None
for word,count in counts.items():
    if count>Bigcount:
        Bigword=word
        Bigcount=count
print('Mail ID:',Bigword,'No of mails:',Bigcount)
