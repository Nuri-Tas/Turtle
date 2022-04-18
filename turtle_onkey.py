import colorgram

hirst_colors = colorgram.extract('hirst_25.jpg', 25)

colors = []
for i in range(25):
    color = hirst_colors[i]
    rgb = color.rgb
    colors.append(rgb)
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

def to_right():
     john.dot(20, random.choice(rgb_colors))
     john.forward(50)

def to_upward():
    y += 30

my_screen.onkey(to_right, "End")
my_screen.onkey(to_upward, "Up")

