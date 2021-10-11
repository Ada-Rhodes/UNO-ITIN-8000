# taken from https://www.geeksforgeeks.org/turtle-programming-python/
import turtle
colors = ['red', 'purple', 'blue', 'green', 'orange', 'yellow']
angle = input('turn degrees?')
t = turtle.Pen()
turtle.bgcolor('black')
t.speed(10000)
for x in range(360):
    t.pencolor(colors[x%6])
    t.width(x//100 + 1)
    t.forward(x)
    t.left(float(angle))