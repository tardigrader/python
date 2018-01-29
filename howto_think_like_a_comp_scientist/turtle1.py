import turtle

window_color = input("What background color do you want? ")
tess_color = input("What color do you want Tess to be? ")
pen_width = int(input("And finally, what pensize do you wish? "))

wn = turtle.Screen()
wn.bgcolor(window_color)      # Set the window background color
wn.title("Hello, Tess!")      # Set the window title

tess = turtle.Turtle()
tess.color(tess_color)            # Tell tess to change her color
tess.pensize(pen_width)               # Tell tess to set her pen width

tess.forward(50)
tess.left(120)
tess.forward(50)

wn.mainloop()
