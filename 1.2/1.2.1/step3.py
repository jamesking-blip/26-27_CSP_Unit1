#a121_catch_a_turtle.py
#-----import statements-----
import turtle as trtl
import random as rand

#-----game configuration----
spot_color = "blue"
spot_size = 4
spot_shape = "arrow"

score = 0

#-----initialize turtle-----
spot = trtl.Turtle()
spot.shape(spot_shape)
spot.shapesize(spot_size)
spot.color(spot_color)


score_writer = trtl.Turtle()
score_writer.shapesize(spot_size)
score_writer.goto(100,100)
#-----game functions--------
def spot_clicked(x, y):
    change_postition()
    update_score()

def change_postition():
    new_xpos = rand.randint(-200, 200)
    new_ypos = rand.randint(-150, 150)
    spot.goto(new_xpos, new_ypos)

def update_score():
    global score
    print("Score " + str(score))
    score += 1
#-----events----------------
spot.onclick(spot_clicked)



wn = trtl.Screen()
wn.mainloop()

















#-----events----------------