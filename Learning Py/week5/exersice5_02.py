num=0
sum=0
while True :
    sval=input('Enter the number')
    if sval=='done' :
        break
    try:
        fval=float(sval)
    except:
        print('invalid input')
        continue
    num=num+1
    sum=sum+fval
#print('Done!')
print(num,sum,sum/num)
