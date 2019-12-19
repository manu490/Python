def hello(greetings, *args):
    if(len(args)==0):
        print(greetings)
    else:
        print(greetings, *args)

hello('hi')
hello('hi','sarah')
