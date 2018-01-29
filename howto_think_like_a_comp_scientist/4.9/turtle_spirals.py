import turtle

wm = turtle.Screen()
wm.bgcolor("lightgreen")

spiral = turtle.Turtle()
spiral.color("blue")
spiral.speed(300)

for i in range(100):
    spiral.forward(2*i)
    spiral.right(90)

wm.mainloop()
