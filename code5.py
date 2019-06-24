a=int(input())
b=0
for i in range(a):
    a=int(a/10)
    b=b+1
    if a==0:
        break


print("თქვენ მიერ შეყვანილი რიცხვი არის",b, "ნიშნა")