'''Create an etch a sketch program

Have the user enter a pen color, a line length, and an angle

Use turtle to draw a line based on their specifications

Let them specify new lines over and over until they enter a 
line length of 0

When the user specifies a line length of 0 stop drawing'''

import turtle
#initializes length
length = 1
while length != 0:
    #asks what color pen to use and sends to turtle
    color=input("What color pen would you like to use? ")
    turtle.color(color)
    #Asks which direction the user would like to move
    move=input("Which direction would you like to move? forward or backward? ")
    #Asks the length of the line
    length=int(input("How long would you like your line to be? "))
    #If the length is 0, the while loop breaks 
    if length==0:
        break
    #if statement to determine direction
    if move=="forward":
        turtle.forward(length)
    elif move=="backward":
        turtle.backward(length)
    #Error handling in case not valid input
    else:
        print("That is not a valid direction")
        move=input("Which direction would you like to move? forward or backward? ")
    #Ask turn direction and angle
    turn=input("Which direction would you like to turn? left or right? ")
    angle=int(input("How many degrees would you like to turn? "))
    #if statement to determine turn and angle
    if turn=="right":
        turtle.right(angle)
    elif turn=="left":
        turtle.left(angle)
    #Error handling
    else:
        print("That is not a valid direction")
        turn=input("Which direction would you like to turn? left or right? ")
 #Messages once while loop breaks   
print("Thank you for playing with the etch a sketch")
print("Since you stated you wanted a length of 0, the program has completed")
print("Have a great day")