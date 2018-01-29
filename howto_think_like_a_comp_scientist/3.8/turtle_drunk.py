import turtle

wn = turtle.Screen()

nerd = turtle.Turtle()

for x in [160, -43, 270, -97, -43, 200, -940, 17, -86]:
    nerd.forward(100)
    nerd.right(x)

drunk_position = nerd.position()
drunk_heading = nerd.heading()

nerd.write("Drunk at " + str(drunk_position) + "\nHeading this way: " + str(drunk_heading))

wn.mainloop()
