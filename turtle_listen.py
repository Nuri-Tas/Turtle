rgb_colors = []
for i in range(25):
    rgb_tuple = (colors[i][0],colors[i][1],colors[i][2])
    rgb_colors.append((rgb_tuple))

print(rgb_colors)

from turtle import Turtle, Screen
import random

my_screen = Screen()
my_screen.colormode(255)
my_screen.listen()

john = Turtle()
john.shape("circle")
john.penup()
john.speed("fastest")

x = -100
y = -100
def right():
     john.dot(20, random.choice(rgb_colors))
     john.forward(50)

print(i)
row()

my_screen.exitonclick()