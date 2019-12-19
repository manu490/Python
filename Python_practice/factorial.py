def fact(n):
    if(n==1):
        return 1
    else:
        return n* fact(n-1)

#Factorial of N = N*N-1*N-2....*1
#finding factorial using recursion in python3
number=int(input('Enter number to find factorial : '))
print('factorial of number ',number, 'is',fact(number))
