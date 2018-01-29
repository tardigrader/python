import turtle

wm = turtle.Screen()

clock = turtle.Turtle()
clock.shape("turtle")

for x in range(12):
    clock.stamp()
    clock.right(28)
    clock.forward(50)

wm.mainloop()
