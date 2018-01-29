# Draw an 18-sided polygon

import turtle

wm = turtle.Screen()
testudo = turtle.Turtle()
testudo.pensize(2)

testudo.penup()
testudo.sety(200)
testudo.pendown()

for x in range(18):
   testudo.forward(75)
   testudo.right(20)

testudo.penup()
testudo.setpos(0,-25)
testudo.pendown()
testudo.hideturtle()
testudo.write("18-sided polygon")

wm.mainloop()
