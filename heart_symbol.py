"""
Project Name: Heart Symbol
Developer Name: Truston Ailende
Email Address: trustonailende@gmail.com
"""
import turtle
import math
 
# Square
def drawSquare(length):
    turtle.penup()
    turtle.setposition(-length/2.0, length/2.0)
    turtle.pendown()
    for i in range(0, 4):
        turtle.forward(length)
        turtle.right(90)
    turtle.penup()
    turtle.home()
 
# Horizontal lines
def drawHorizontalLine(length, division):
    pixelSpace = int(length / division)
    half = int(length / 2)
    for j in range((-half + pixelSpace), half, pixelSpace):
        turtle.penup()
        turtle.setposition(-half, j)
        turtle.pendown()
        turtle.forward(length)
    turtle.penup()
    turtle.home()
 
# Vertical lines
def drawVerticalLine(length, division):
    pixelSpace = int(length / division)
    half = int(length / 2)
    turtle.right(90)
    for k in range((-half + pixelSpace), half, pixelSpace):
        turtle.penup()
        turtle.setposition(k, half)
        turtle.pendown()
        turtle.forward(length)
    turtle.penup()
    turtle.home()
 
# Draw the grid
turtle.speed(0)
drawSquare(400)
drawHorizontalLine(400, 40)
drawVerticalLine(400, 40)
 
# Change the colour mode
turtle.colormode(255)
 
# Change the pencolor to red
turtle.pencolor(255, 0, 0)
 
# Draw the horizontal centre line
turtle.setposition(-200, 0)
turtle.pendown()
turtle.forward(400)
turtle.penup()
 
# Draw the vertical centre line
turtle.setposition(0, 200)
turtle.setheading(270)
turtle.pendown()
turtle.forward(400)
 
# Reset all the properties
turtle.home()
turtle.pencolor(0, 0, 0)
 
# Place code here

turtle.color('red', 'red')

# Lift up the pen
turtle.penup()

# Move the turtle to the top right middle position
turtle.setposition(-100, 100)

# Place the pen down
turtle.pendown()

# Set the heading of the turtle to 90 degrees
turtle.setheading(90)

turtle.begin_fill()

# Draw a semi-circle of radius 50 from left to right
turtle.circle(-50, 180)

# Set the heading of the turtle to 90 degrees
turtle.setheading(90)

# Draw another semi-circle of radius 50 from left to right
turtle.circle(-50, 180)

# Draw a sector from position (100, 100) down to the center line
turtle.circle(-200, 60)

# Lift up the pen
turtle.penup()

# Move the pen to the position (-100, 100)
turtle.setposition(-100, 100)

# Place the pen down
turtle.pendown()

# Change the heading of the pen to 180 degrees
turtle.setheading(270)

# Draw a sector from position (-100, 100) down to the center line
turtle.circle(200, 60)

turtle.end_fill()

# End the program
turtle.hideturtle()
