import turtle

wm = turtle.Screen()
wm.bgcolor("lightgreen")

spiral = turtle.Turtle()
spiral.color("blue")
spiral.speed(300)

for i in range(100):
    spiral.forward(i+2)
    spiral.left(271)

wm.mainloop()
