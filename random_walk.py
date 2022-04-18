from turtle import Turtle, Screen
import random

john = Turtle()

def move(name):
    if name == "r":
        john.right(90)
        john.forward(20)
    if name == "l":
        john.left(90)
        john.forward(20)
    if name == "f":
        john.forward(20)
    if name == "b":
        john.backward(20)

directions = ["r", "l", "f", "b"]

size = 1
speed = 1
for i in range(1000):
    direction_is = random.choice(directions)
    color = random.choice(colors)
    john.color(color)
    move(direction_is)
    print(color)
    size += 1
    speed += 1
    john.pensize(size)
    john.speed(speed)



my_screen = Screen()
my_screen.exitonclick()
