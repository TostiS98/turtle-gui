#TostiS98
#12/7/18

#import libraries
from random import randint
import random
import turtle

#Greet the user
print("-"*52)
print ("Welcome to my first ever trial in the world of GUI's")
print("-"*52)
print ("> Clicking in the top left quadrant results in a square")
print("> Clicking in the top right quadrant results in a triangle")
print("> Clicking in the bottom left quadrant results in a circle")
print("> Clicking in the bottom right quadrant results in a pentagon")
print("> Each time the program is run, a screen of randomized dimensions will appear")
print("> The screen will also have a randomized background colour and turtle colour")


#Create a turtle object
t = turtle.Turtle ()

def main():
   # Create a screen that has a randomized size, between 500 and 900 for the x and y dimensions
   x = random.randint (500,900)
   y = random.randint (500,900)
   turtle.setup(x,y)

   # Inside the frame, create a window known as "window"
   window = turtle.Screen()

   # Give the window a title that is personal
   window.title("TostiS98 - Turtle GUI")
  
  
   #Define all of the necessary variables with the cooresponding outcomes of the functions
   background_colour = pick_background ()
  
   window.bgcolor(background_colour)

   t.color(pick_turtle_colour())
   t.pensize(pick_pensize())
   window.onclick(leftclick_time)
   
#Create a function that randomizes the background colour of the window    
def pick_background():
    colour_list = ['yellow','red','blue','orange','pink']
    number_chosen = randint(0,4)
    colour_chosen = colour_list[number_chosen]
    return colour_chosen

#Create a function that randomizes the turtles colour
def pick_turtle_colour():
    colour_list = ['light blue','light green','Grey','Black','Turquoise']
    number_chosen = randint(0,4)
    colour_chosen = colour_list[number_chosen]
    return (colour_chosen)
   

#Define a function to choose the pensize of the turtle
def pick_pensize():
    size_list = [1,2,3,4,5]
    number_chosen = randint(0,4)
    pen_size = size_list[number_chosen]
    return (pen_size)
    

#Create a function that commands the turtle to move cooresponding to the users click on the screen
def leftclick_time (x, y):
    t.goto (x, y)
    
#Create an if statement that draws a square if the mouse is clicked in the top left quadrant
    if ((t.xcor () <= 0) and (t.xcor () >= -900) and (t.ycor () >=0) and (t.ycor () <= 900)):
        draw_square()


#Create an if statement that draws a triangle if the mouse is clicked in the top right quadrant
    if ((t.xcor () > 0) and (t.xcor () < 901) and (t.ycor () >0) and (t.ycor () < 901)):
        draw_triangle()
        
#Create an if statement that draws a circle if the mouse is clicked in the bottom right quadrant
    if ((t.xcor () < 0) and (t.xcor () > -901) and (t.ycor () <0) and (t.ycor () > -901)):
        draw_circle()
       
#Create an if statement that draws a pentagon if the mouse is clicked in the bottom left quadrant of the screen
    if  ((t.xcor () > 0) and (t.xcor () < 901) and (t.ycor () <0) and (t.ycor () > -901)):
        draw_pentagon()
       
def draw_square():
    t.clear ()
    t.goto (0,0)
    t.clear ()
    t.goto (-100,0)
    t.goto (-100,100)
    t.goto (0,100)
    t.goto (0, 0)
    t.clear()
    
def draw_triangle():
    t.clear ()
    t.goto (0,0)
    t.clear ()
    t.goto (100,0)
    t.goto (50,50)
    t.goto (0,0)
    t.clear()
        
    
def draw_circle():
    t.clear ()
    t.goto (0,0)
    t.clear ()
    t.circle (50)
    t.clear()
    
def draw_pentagon():
    t.clear()
    t.goto (0,0)
    t.clear()
    t.goto (-50, -50)
    t.goto (-25,-100)
    t.goto (25,-100)
    t.goto (50,-50)
    t.goto (0,0)
    t.clear()

main ()
