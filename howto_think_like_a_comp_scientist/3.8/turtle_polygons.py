import turtle

wn = turtle.Screen()

nerd = turtle.Turtle()

# Triangle
for x in range(3):
   nerd.forward(100)
   nerd.left(120)

nerd.penup()
nerd.home()
nerd.right(90)
nerd.forward(50)
nerd.pendown()

# Square
for x in range(4):
    nerd.forward(100)
    nerd.right(90)

nerd.penup()
nerd.left(90)
nerd.forward(50)
nerd.pendown()

# Hexagon
for x in range(6):
    nerd.forward(60)
    nerd.right(60)

nerd.penup()
nerd.forward(150)
nerd.pendown()

# Octagon
for x in range(8):
    nerd.forward(45)
    nerd.right(45)

wn.mainloop()
