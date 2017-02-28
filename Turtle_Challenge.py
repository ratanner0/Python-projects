'''Get turtle to draw an octagon

Hint: to calculate the angle, you take 360 degrees and 
divide it by the number of side of the shape you are drawing

Extra Challenge: Let the user specify how many sides the 
object will have and draw whatever they ask

Double bonus challenge: add a nested loop to draw a smaller 
version of the object'''
#imports the turtle module
import turtle
#asks the user how many sides they would like to have and stores as an int
sides=int(input("How many sides would you like your shape to have? "))
#lets the user choose the color of the shape
color=input("What color would you like your shape to be? ")

for steps in range (sides):
    turtle.color(color)
    turtle.forward(100)
    turtle.right(360/sides)
    #this code makes it to where only one smaller object is printed
    if steps == sides-1:
        #smaller version of object
        for smaller in range (sides):
            turtle.forward(50)
            turtle.right(360/sides)
    else:
        continue