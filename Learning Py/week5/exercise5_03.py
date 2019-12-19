Largest=None
Smallest=None
while True:
    inp=input("Enter the Integer")
    if inp=='done':
        break
    try:
        num=int(inp)
    except:
        print("Invalid input")
    else:
        if Smallest is None:
            Smallest=num
            Largest=num
        elif num<Smallest:
            Smallest=num
        elif num>Largest:
            Largest=num
print("Maximum",Largest)
print("Minimum",Smallest)
