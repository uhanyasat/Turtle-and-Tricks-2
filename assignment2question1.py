# INCLUDE YOUR NAME
# INCLUDE YOUR MIT ID


import turtle
import random

list_of_turtles=[]#list to hold all the turtles


obj=turtle.Turtle()#TESTING TO CREATE A NEW TURTLE
obj.shape('turtle')#TESTING TO LET IT LOOK LIKE ONE!


obj.forward(20)#TESTING THE MOVEMENT FORWARD
obj.right(90)#TESTING THE MOVEMENT TO IT'S RIGHT
obj.forward(100)
obj.right(90)

obj.circle(50)#TESTING THE MOVEMENT OF CIRCLE
##
##def setup():
##    global turtles
##    start_line=-320# Currently the starting position is incorrect! You need to fix it.
##    screen=turtle.Screen()
##    screen.setup(930,547)
##    screen.bgpic('pavement.gif')#THIS IMAGE SHOULD BE IN THE FOLDER WHERE THIS SCRIPT IS.
##
##    turtle_ycor=[-40,-20,0]
##    turtle_color=['blue','red','green']
##
##    for i in range(0,len(turtle_ycor)):
##        new_turtle=turtle.Turtle()
##        new_turtle.shape('turtle')
##        new_turtle.penup()
##        new_turtle.setpos(start_line,turtle_ycor[i])
##        new_turtle.color(turtle_color[i])
##        new_turtle.pendown()
##        list_of_turtles.append(new_turtle)
##
##def race():
##    global turtles
##    winner=False
##    finishLine=590
##    while not winner:
##        for current_turtle in list_of_turtles:
##            move=random.randint(0,2)
##            current_turtle.forward(move)
##
##            xcor=current_turtle.xcor()
##            #if (xcor>=#MISSING CODE#):
##                #MISSING CODE#
##                #MISSING CODE#
##                #MISSING CODE#
##def main():
##
##    setup()
##    race()
##    turtle.mainloop()
##
##
##main()
