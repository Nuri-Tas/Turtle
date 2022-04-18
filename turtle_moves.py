from turtle import Turtle, Screen
import random
turtle = Turtle()

colors = ["red", "blue", "yellow", "black", "purple", "pink", "turquoise", "green"]
angles = [120, 90, 72, 60, 360/7, 360/8, 360/9, 36]
angle_element = 0

k = 3
for i in range(8):
    turtle.pencolor(random.choice(colors))
    for j in range(k):
        turtle.forward(50)
        turtle.right(angles[angle_element])
    k += 1
    angle_element += 1

print(k)


screen = Screen()
screen.exitonclick()