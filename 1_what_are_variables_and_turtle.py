import turtle

my_turtle = turtle.Turtle()


# this is a square
def square():
    my_turtle.forward(100)
    my_turtle.right(90)
    my_turtle.forward(100)
    my_turtle.right(90)
    my_turtle.forward(100)
    my_turtle.right(90)
    my_turtle.forward(100)


square()
my_turtle.forward(100)
square()

input()
