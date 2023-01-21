import turtle
t=turtle.Turtle()
screen=turtle.getscreen()
screen.setup(420,320)
turtle.bgcolor("black")
t.pencolor("red")
t.pensize(4)
t.shape("turtle")
n=0
while n<=7:
    n=n+1
    t.penup()
    t.setpos(0,-n*20)
    t.pendown()
    t.circle(20*n)

