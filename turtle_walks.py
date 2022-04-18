from turtle import Turtle, Screen
import random

john = Turtle()
my_screen = Screen()
my_screen.colormode(255)
john.width(7)

def turtle_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    our_color = (r,g,b)
    return john.color(our_color)

directions = [0, 90, 180, 270]
def move():
    john.setheading(random.choice(directions))
    john.forward(15)

for i in range(200):
    turtle_color()
    move()

my_screen.exitonclick()