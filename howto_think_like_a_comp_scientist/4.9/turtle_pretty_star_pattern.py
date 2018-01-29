import turtle

wm = turtle.Screen()
wm.bgcolor("lightgreen")

star = turtle.Turtle()
star.color("blue")
star.pensize(2)
star.speed(200)

for i in range(20):
    # Draw a rectangle
    for i in range(4):
        star.forward(100)
        star.right(90)
#        star.forward(100)
    star.right(18)          # Rotate rectangle 18 degrees
                            # (because 360/20 = 18)

wm.mainloop()
