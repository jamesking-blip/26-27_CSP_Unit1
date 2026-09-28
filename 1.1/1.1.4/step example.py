#   a114_nested_loops_2.py
import turtle as trtl

color1 = "orange"
color2 = "Blue"

wn = trtl.Screen()
width = 400
height = 300

painter = trtl.Turtle()
painter.speed(0)
painter.color(color1)
#start assuming we will draw
answer = "y"
#Loop imtil the user is bored
while (answer == "y"):
#erase what is on the current window
  wn.clearscreen()
  painter.goto(0,0)
  #Set up the space counter
  space = 1

  angle = int(input("angle:"))
  seg = int(360/angle)
  # CODE TO ADD
  while painter.ycor() < height:
      if space % 100:
          painter.fillcolor(color2)
          painter.color(color2)
      if space % 200 == 0:
          painter.fillcolor(color1)
          painter.color(color1)
      painter.speed(100)
      painter.right(angle)
      painter.forward(2 * space + 10)  # experiment
      painter.begin_fill()
      painter.circle(3)
      painter.end_fill()
      space = space + 1
  answer = input("again?")

wn.bye()

