"""
LeagueBot

Write your own turtle program! Here is what your program should do

1) Change the turtle image to 'leaguebot_bot.gif'
2) Change the turtle size to 10x10
3) Change the turtle line color to 'blue'
4) Draw a hexagon using a loop and variables.
"""

import turtle
turtle.setup(600, 600, 0, 0)
# Set up the screen
screen = turtle.Screen()
screen.setup(width=600, height=600)


# Create a turtle and set its shape to the custom GIF
t = turtle.Turtle()
t.shape("turtle")
t.turtlesize(10)
t.pencolor("blue")
def draw_polygon(sides):

    angle =360/sides                             # Calculate angle from number of sides
    
    for i in range(8):                 # Loop through the number of sides
        t.forward(100)
        t.left(angle)



draw_polygon(8)

# Move the turtle to each corner of the screen in a square pattern

turtle.exitonclick() 




