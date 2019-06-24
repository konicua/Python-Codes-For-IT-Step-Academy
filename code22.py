import turtle

STAR_SIZE = 100

EXPANSION = 1.2
TRANSLATION = STAR_SIZE * EXPANSION / 4

turtle.hideturtle()
turtle.color("black")
turtle.shape("triangle")
turtle.turtlesize(STAR_SIZE * EXPANSION / 20)

for _ in range(5):
    turtle.right(72)
    turtle.forward(TRANSLATION)
    turtle.stamp()
    turtle.backward(TRANSLATION)