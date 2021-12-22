import turtle

s =turtle.Screen().bgcolor('black')
t =turtle.Turtle()
t.speed(30)
t.width(20)



print("MOHD AQIB")

def curve():
    for i in range(200):
        t.right(1)
        t.forward(1)

def hearth():
    t.color('red' ,'red')
    t.begin_fill()
    t.left(140)
    t.forward(113)
    curve()
    t.left(120)
    curve()
    t.forward(112)
    t.end_fill

hearth()
t.pencolor('black')
t.penup()
t.goto(0,170)
t.pendown()
for zigzag in range(2):
    t.left(75)
    t.forward(40)
    t.left(40)
    t.forward(40)
    print('hello')