# Draw a five-pointed star

import turtle

wm = turtle.Screen()

occult = turtle.Turtle()
# Five points = 360/5 = 72 degrees

for x in range(5):
    occult.left(72)
    occult.forward(150)
    occult.right(144)
    occult.forward(150)

wm.mainloop()
