# CODE TO COPY
#   a118_turtles_in_traffic.py
#   Move turtles horizontally and vertically across screen.
#   Stopping turtles when they collide.


import turtle as trtl

# create two empty lists of turtles, adding to them later
horiz_turtles = []
vert_turtles = []

# use interesting shapes and colors
turtle_shapes = ["arrow", "turtle", "circle", "square", "triangle", "classic"]
horiz_colors = ["red", "blue", "green", "orange", "purple", "gold"]
vert_colors = ["darkred", "darkblue", "lime", "salmon", "indigo", "brown"]
#tloc will be added to where ever it is put
tloc = 50
#Make a loop to print the turtles
for s in turtle_shapes:
    ht = trtl.Turtle(shape=s)
    horiz_turtles.append(ht)
    ht.penup()
    new_color = horiz_colors.pop()
    ht.fillcolor(new_color)
    ht.goto(-350, tloc)
    ht.setheading(0)

    #This gives each turtle its colors
    vt = trtl.Turtle(shape=s)
    vert_turtles.append(vt)
    vt.penup()
    new_color = vert_colors.pop()
    vt.fillcolor(new_color)
    vt.goto(-tloc, 350)
    vt.setheading(270)





    # all of this is to get the turtles into the postitions they are in
    tloc += 50

#Do: move turtles across and down screen, stopping for collisions



for step in range(50):


# Loop through all horizontal turtles in the list
    for ht in horiz_turtles:
        for vt in vert_turtles:
            ht.forward(10)
            vt.forward(10)

            if (abs(ht.xcor() - vt.xcor()) <= 40):
                if (abs(ht.ycor() - vt.ycor()) <= 40):

                    horiz_turtles.remove(ht)
                    vert_turtles.remove(vt)
                    ht.fillcolor("gray")
                    vt.fillcolor("gray")




wn = trtl.Screen()
wn.mainloop()




