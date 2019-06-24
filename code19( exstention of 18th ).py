import  turtle

bro = turtle.Turtle()
secondbro = 100
bro.speed(10)
a = int(input("number"))
for i in range(a*2):
    secondbro = secondbro+10
    bro.forward(secondbro)
    bro.right(90)
    bro.forward(secondbro)
    bro.right(90)
input()