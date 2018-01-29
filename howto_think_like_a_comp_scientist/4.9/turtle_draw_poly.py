import turtle

# Draw polygon with turtle t, number of sides n and size sz
def draw_poly(t, n, sz):
    for i in range(n):
        t.forward(sz)
        t.right(360/n)

wm = turtle.Screen()

tess = turtle.Turtle()

draw_poly(tess, 4, 50)

wm.mainloop()
