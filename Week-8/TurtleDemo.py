# tutorial adapted from https://www.youtube.com/watch?v=WiShwgtWWHI
from turtle import * # WHY DID I NEVER KNOW THIS


speed(2) #speed of the "turtle"
bgcolor("black") #color of the background
color("orange") #color of the line
pensize(1) #thickness of the line

for i in range(8):
    forward(100)
    left(45)