#draw spiral triangle
import turtle
t=turtle.Turtle()
side=150
for i in range(50):
    t.bk(side)
    t.right(120)
    side=side-3
