# Draw a pentagram

import turtle

wm = turtle.Screen()

pentagram = turtle.Turtle()
pentagram.pensize(3)
pentagram.hideturtle()

# Five points = 360/5 = 72 degrees

pentagram.left(72)
pentagram.forward(150)
pentagram.right(144)
pentagram.forward(150)
pentagram.left(-144)
pentagram.forward(150)
pentagram.right(144)
pentagram.forward(150)
pentagram.left(-144)
pentagram.forward(150)

# Draw the circle around the star
pentagram.penup()
pentagram.setpos(-2.5,130)
pentagram.pendown()
pentagram.circle(82.5)

wm.mainloop()
