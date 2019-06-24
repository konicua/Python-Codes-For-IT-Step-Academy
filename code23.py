import turtle
turtle.shape('turtle')

def triangle():
    for i in range(3):
        turtle.forward(50)
        turtle.right(360/3)


def square():
    for i in range(4):
        turtle.forward(50)
        turtle.right(360/4)

def pentagon():
    for i in range(5):
        turtle.forward(50)
        turtle.right(360/5)


answer = input('pick a shape.. triangle, square or pentagon')
if answer ==('triangle'):
    triangle()

elif answer == ('square'):
    square()

elif answer == ('pentagon'):
    pentagon()

else:
    print ('wrong input')