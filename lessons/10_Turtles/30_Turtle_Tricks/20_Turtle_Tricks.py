"""
# 20_Turtle_Tricks.py

In this assignment, you will use Tina the Turtle to draw a pentagon. 

- Each side of the pentagon should be a different color. 
- Use the turtle commands: tina.forward(), tina.left(), and tina.pencolor() to accomplish this.

Refer to the previous program, Meet_Tina.py, for examples of how to use turtle commands.
"""

# These lines are needed in most turtle programs
import turtle                           # Tell Python we want to work with the turtle
turtle.setup(600, 600, 0, 0)            # Set the size of the window
tina = turtle.Turtle()                  # Create a turtle named tina

# Use tina.forward() and tina.left() to draw a pentagon
# Make each side of the pentagon a different color with 
# tina.pencolor()

... # Your code here
import turtle
turtle.setup(600,600,0,0)
tina = turtle.Turtle()                    # Close the window when we click on it


tina.forward(100)
tina.pencolor('green')
tina.left(60)
tina.forward(100)
tina.left(60)
tina.forward(100)
tina.right(120)
tina.forward(200)
tina.right(60)
tina.forward(100)
turtle.exitonclick()