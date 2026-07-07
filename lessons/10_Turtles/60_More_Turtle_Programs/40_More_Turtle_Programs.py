"""
Copy the code from the previous lesson, 10_More_Turtle_Programs.ipynb,
from the section "Clicking the Turtle Directly"

Then change the code so that the turtle has a different image ( look in the 'images'
directory ) and when you click on it, it moves to a random location on the screen.

Use this code to get a random x and y location

    import random
    x = random.randint(-300, 300)
    y = random.randint(-300, 300)
"""


import turtle
import random
t.shape("turtle")
def set_turtle_image(turtle,emoji):
    """Set the turtle's shape to a custom image."""

    from pathlib import Path                        # Import Path from pathlib module
    image_dir = Path(__file__).parent.parent / "images"    # Define the directory containing images
    image_path = str(image_dir /emoji)        # Create the full path to the image file

    screen = turtle.getscreen()                     # Get the turtle's screen
    screen.addshape(image_path)                     # Register the image as a shape
    turtle.shape(image_path)    

def set_background_image(window, image_name):
    """Set the background image of the turtle window to the image with the given name."""
    from pathlib import Path                                        # Import Path from pathlib module
    from PIL import Image                                           # Import Image from PIL (Pillow) library

    image_dir = Path(__file__).parent / "images"                    # Define the directory containing images
    image_path = str(image_dir / image_name)                        # Create the full path to the image file

    image = Image.open(image_path)                                  # Open the image to get its dimensions
    
    window.setup(image.width, image.height, startx=0, starty=0)     # Set window size to image size
    window.bgpic(image_path)                                                            # Set the turtle's shape to the image

# Set up the screen
screen = turtle.Screen()
screen.setup(width=600, height=600)

# Create a turtle and set its shape to the custom GIF
t = turtle.Turtle()

set_turtle_image(t,"pikachu.gif")

t.penup()   # Prevent drawing when moving
t.speed(3)  # Set a moderate speed

# Move the turtle to each corner of the screen in a square pattern
for x, y in [(200, 200), (200, -200), (-200, -200), (-200, 200)]:
    t.goto(x, y)
x = random.randint(-300,300)
y = random.randint(-300,300)
# Double-click to copy!

                                           

t.turtlesize(stretch_wid=10, stretch_len=10, outline=4)     # Make the turtle really big

def turtle_clicked(t, x, y):
    """Function that gets called when the user clicks on the turtle

    This function will make the turtle tilt 20 degrees 18 times, making a full
    circle. It is called by the turtle when the user clicks on it.

    Args:
        t (Turtle): The turtle object that was clicked
        x (int): The x coordinate of the click
        y (int): The y coordinate of the click
    """

    print('turtle clicked!')
    
    for i in range(0,360, 20):  # Full circle, 20 degrees at a time
        print(i)
        t.tilt(20)              # Tilt the turtle 20 degrees

# Connect the turtle to the turtle_clicked function
t.onclick(lambda x, y, t=t: turtle_clicked(t, x, y))

turtle.done() # Important! Use `done` not `exitonclick` to keep the window open




