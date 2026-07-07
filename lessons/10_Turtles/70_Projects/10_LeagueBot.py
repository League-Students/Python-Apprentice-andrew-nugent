"""
LeagueBot

Write your own turtle program! Here is what your program should do

1) Change the turtle image to 'leaguebot_bot.gif'
2) Change the turtle size to 10x10
3) Change the turtle line color to 'blue'
4) Draw a hexagon using a loop and variables.
"""

import turtle
# Set up the screen
screen = turtle.Screen()
screen.setup(width=600, height=600)

# Create a turtle and set its shape to the custom GIF
t = turtle.Turtle()
t.size(10)
t.shape("turtle")

t.penup()   # Prevent drawing when moving
t.speed(3)  # Set a moderate speed

# Move the turtle to each corner of the screen in a square pattern

turtle.exitonclick() 




