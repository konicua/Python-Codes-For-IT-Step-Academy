import turtle

t1 = turtle.Turtle()

screen = turtle.Screen()

screen.bgcolor("blue")

t1.color("light green")
t1.fillcolor("green")
t1.pensize(3)
t1.up()
t1.goto(0, -150)
t1.down()
t1.begin_fill()
t1.fd(100)
tree_branch_length = 50

for tree_loop_L in range (5):
    t1.fd(tree_branch_length)
    t1.left(120)
    t1.fd(100)
    t1.left(-120)
    tree_branch_length = tree_branch_length - 10

tree_branch_length = -10
t1.left(240)

for tree_loop_R in range (5):
    t1.fd(100)
    t1.left(-60)
    t1.fd(tree_branch_length)
    t1.left(60)
    tree_branch_length = tree_branch_length - 10

t1.left(-240)
t1.fd(150)
t1.end_fill()