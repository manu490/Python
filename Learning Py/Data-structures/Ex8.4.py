fname = input("Enter file name: ")
fh = open(fname)
lst=list()
for line in fh:
   word=line.rstrip().split()
   for item in word:
       if item in lst:
           continue
       else:
           lst.append(item)
lst.sort()
print(lst)
