# Draw a five-pointed "shuriken" 

import turtle

wm = turtle.Screen()

shuriken = turtle.Turtle()
shuriken.speed(0)

for x in range(5):
    shuriken.left(72)
    shuriken.forward(150)
    shuriken.right(144)
    shuriken.forward(150)
    shuriken.right(72)
    shuriken.forward(150)

wm.mainloop()
