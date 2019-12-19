# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
try:
    fh = open(fname)
except:
    print('file not found')
    quit()
count=0
num=0
Average=0
for line in fh:
    line = line.rstrip()
    if not line.startswith("X-DSPAM-Confidence:") :
        continue
    count=count+1
    Statem=line[19 : ]
    number=float(Statem)
    num=num+number
    #print(Statem)
    #print(num)
Average=num/count
print('Average spam confidence:', Average)
