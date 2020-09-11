#!/usr/bin/env python
# coding: utf-8

'''
Turtle starter code
ATLS 1300
Author: Dr. Z
Author: YOUR NAME
May 29, 2020
'''

from turtle import * #import the library of commands that you'd like to use

colormode(255)

# Create a panel to draw on. 
panel = Screen()
w = 600 # width of panel
h = 600 # height of panel
panel.setup(width=w, height=h) #600 x 600 is a decent size to work on. 
#You can experiment by making it the size of your screen or super tiny!

# Create a colorful background and add Bezos image to it
image = "Bezos.gif"
panel.bgcolor(72,202,228)
panel.bgpic(image)

#=======Add your code here======
speed(10)
hideturtle()
up()
goto(-16,128)
shape("circle")
shapesize(.25)
showturtle()
down()
pencolor(161,2,76)
pensize(4)
setheading(180)
circle(20)
goto(20,124)
setheading(270)
circle(20)
goto(-16,128)
up()
goto(80,200)
pencolor(32,28,53)
pensize(12)
down()
setheading(180)
forward(180)
up()
goto(18,200)
down()
begin_fill()
setheading(90)
forward(75)
left(90)
forward(122)
left(90)
forward(75)
end_fill()




