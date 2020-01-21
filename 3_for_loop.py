import turtle

my_turtle = turtle.Turtle()
my_turtle.speed(10)


# this is a square
def square():
    my_turtle.forward(30)
    my_turtle.right(25)
    my_turtle.forward(30)
    my_turtle.right(25)
    my_turtle.forward(30)
    my_turtle.right(25)
    my_turtle.forward(30)
    my_turtle.right(25)
    my_turtle.forward(30)
    my_turtle.right(25)
    my_turtle.forward(30)
    my_turtle.right(25)
    my_turtle.forward(30)
    my_turtle.right(25)
    my_turtle.forward(30)
    my_turtle.right(25)
    my_turtle.forward(30)


for i in range(30):
    square()

input()
