import turtle
import colorsys

t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor('black')
t.speed(0)
n=200
h=0
t.left(180)
for i in range(360):
    c = colorsys.hsv_to_rgb(h , 1, 0.3)
    h+= 1/n
    t.color(c)
    t.left(144)
    t.forward(i*5)