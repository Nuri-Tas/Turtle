import colorgram

hirst_colors = colorgram.extract('hirst_25.jpg', 25)

colors = []
for i in range(25):
    color = hirst_colors[i]
    rgb = color.rgb
    colors.append(rgb)

print(colors)
print(colors[0])

rgb_colors = []
for i in range(25):
    rgb_tuple = (colors[i][0],colors[i][1],colors[i][2])
    rgb_colors.append((rgb_tuple))

print(rgb_colors)

from turtle import Turtle, Screen
import random

my_screen = Screen()
my_screen.colormode(255)

john = Turtle()
john.shape("circle")
john.penup()
john.speed("fastest")
def row():
    i = 0
    y = -150
    john.setx(-150)
    for j in range(5):
        for i in range(5):
            john.sety(y)
            john.dot(20, random.choice(rgb_colors))
            john.forward(50)
            i += 1
            print(i)
        john.setx(-150)
        y += 30

print(i)
row()

my_screen.exitonclick()