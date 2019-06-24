width = widthofcanvas
horizontal = width
while horizontal > 0:
    draw right for horizontal steps
    draw down for 10 steps
    draw right for horizontal-10 steps
    draw down for 10 steps
    horizontal = horizontal - 20

import turtle
window = turtle.Screen()

pen = turtle.Turtle()
horizontal = 100
while horizontal > 0:
        pen.forward(horizontal)
        pen.right(90)
        pen.forward(10)
        pen.right(90)
        pen.forward(horizontal-10)
        pen.left(90)
        pen.forward(10)
        pen.left(90)
        horizontal -= 20

while horizontal <= 100:
        pen.forward(horizontal)
        pen.right(90)
        pen.forward(10)
        pen.right(90)
        pen.forward(horizontal+10)
        pen.left(90)
        pen.forward(10)
        pen.left(90)
        horizontal += 20

window.exitonclick()