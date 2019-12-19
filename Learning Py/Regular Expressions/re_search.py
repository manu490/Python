import re
hand = open('short.txt')
for line in hand:
    lin=line.rstrip()
    if re.search('^From:',line):
    #RE-" ^ " means starts with
       print(line)
