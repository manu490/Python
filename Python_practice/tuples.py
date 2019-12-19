#Input1: Number of Integer:?
n=int(input('Number of Integers:'))
#Input2:Integers list:?
while True:
    Integrs=input('Enter integers with space between each:')
    int_list=map(int,Integrs.split())
    #convert input into tuples;
    t=tuple(int_list)
    if(len(t)>n):
        print('Entered More than',n,'integers ')
        continue
    if(len(t)<n):
        print('Entered less than',n,'integers ')
        continue
    break
#print the hash value of tuple t;
print(hash(t))
