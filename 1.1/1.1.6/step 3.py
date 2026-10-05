# CODE TO ADD
#   a116_buggy_image.py
import turtle as trtl
# instead of a descriptive name of the turtle such as painter,
# a less useful variable name x is used
x = trtl.Turtle()
#Create a spider body




x.pensize(40)
x.circle(20)
#Configure spider legs
legs = 7
length = 100
Changesdierections = 380 / legs
x.pensize(5)
subtractslegs = 0
#Draw legs
while (subtractslegs < legs):
  x.goto(0,20)
  x.setheading(Changesdierections*subtractslegs)
  x.forward(length)
  subtractslegs = subtractslegs + 1

x.hideturtle()
wn = trtl.Screen()
wn.mainloop()
