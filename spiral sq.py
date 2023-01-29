#spiral  square
import turtle
t=turtle.Turtle()
side=250
t.speed(10)
for i in range(100):
    t.fd(side)
    t.rt(90)
    side=side-2
    t.hideturtle()
    
