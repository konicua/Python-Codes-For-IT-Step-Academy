def Math(a,b):
    c=a
    for i in range(b-1):
        a=a*c
    print(a)


a=int(input())
b=int(input())
Math(a,b)