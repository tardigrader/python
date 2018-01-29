import turtle

def draw_square(t, sz):
    """Make turtle t draw a square of sz."""
    for i in range(5):
        for i in range(4):
            t.down()
            t.forward(sz)
            t.left(90)
            t.up()
        t.up()
        t.forward(sz*2)
wn = turtle.Screen()        # Set up the window and its attributes
wn.bgcolor("lightgreen")
wn.title("Alex meets a function")

alex = turtle.Turtle()      # Create alex
draw_square(alex, 20)       # Call the function to draw the square
wn.mainloop()
