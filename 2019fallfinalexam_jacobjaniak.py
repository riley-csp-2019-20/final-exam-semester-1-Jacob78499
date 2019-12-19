#2019-20 Fall Computer Science Principles Final Exam

#Ms. Haubold


#Name
#Jacob Janiak
#Date
#12/19/19


#### INSTRUCTIONS ####
#Create an etch a sketch turtle game
#The turtle should move with the arrow keys (up, down, left and right), and draw
#Space should clear the screen
#o and p should make the pen size bigger and smaller
#u should pick the pen up or put the pen down
#All code must be commented
#BONUS
#Add a feature to change colors
#

#import required libraries
import turtle as trtl
#create and name turtle
Draw_turtle = trtl.Turtle()
#turtle shape
Draw_turtle.shape("arrow")
#list of letters
letter_list = ["O", "P", "space"]
#Turtle adjustments
Draw_turtle.pensize(5)
#movement functions
def up():
    Draw_turtle.setheading(90)
    Draw_turtle.forward(10)
def down():
    Draw_turtle.setheading(270)
    Draw_turtle.forward(10)
def left():
    Draw_turtle.setheading(180)
    Draw_turtle.forward(10)
def right():
    Draw_turtle.setheading(0)
    Draw_turtle.forward(10)
def o():
  if ("O" in letter_list):
      Draw_turtle.pensize(+5)
def p():
    if ("P" in letter_list):
        Draw_turtle.pensize(-5)
def space():
    if ("space" in letter_list):
        wn.clearscreen() 
#color/drawing functions

#create screen
wn = trtl.Screen()
#bind to keypresses
wn.onkeypress(up, "Up")
wn.onkeypress(down, "Down")
wn.onkeypress(left, "Left")
wn.onkeypress(right, "Right")
wn.onkeypress(o, "O")
wn.onkeypress(p, "P")
wn.onkeypress("space")
#listen
wn.listen()
#mainloop
wn.mainloop()