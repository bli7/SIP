from turtle import *
import math

# Name your Turtle.
t = Turtle()

# Set Up your screen and starting position.
setup(500,300)
x_pos = 0
y_pos = 0
t.setposition(x_pos, y_pos)

input_text = input("How many sides do you want?")
sides = int(input_text)

color_text = input("What color do you want?")

def draw():
    for i in range(sides):
        pendown()
        pencolor(color_text)
        forward(50)
        right(360 / sides)

draw()

exitonclick()
