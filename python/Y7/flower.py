# flower.py
# turtle flower based on example in "Mindstorms".

from turtle import *

def main():
    pen = Turtle(visible = False)
    pen.speed(50)
    #draw some "earth"
    pen.pu()
    pen.goto(-100, -200)
    pen.pd()
    pen.pencolor("brown")
    pen.pensize(4)
    pen.fd(200)
    pen.back(100)
    # prepare to draw flower.
    pen.lt(90)
    pen.pensize(3)
    plant(pen, 5, "blue", 60)

def quarterC(pen, r):
    """Quarter circle function. Takes a turtle object and a radius.
    Calculates steps based on the circumference."""
    step = r * 0.02
    for i in range(90):
            pen.right(1)
            pen.fd(step)

def petal(pen, p):
    """Draws two quarter circles one on top of the other."""
    quarterC(pen, p)
    pen.right(90)
    quarterC(pen, p)
    pen.right(90)

def flower(pen, n, size):
    """Draws a flower from 'n' petals of size 'size'."""
    for i in range(n):
        petal(pen, size)
        pen.right(360/n)
        
def plant(pen, n, col, h):
    """Draws a stalk, a leaf and then switches to the colour for the flower."""
    pen.pencolor("dark green")
    pen.fd(h)
    petal(pen, h)
    pen.fd(h*3)
    pen.pencolor(col)
    flower(pen, n, h)
    
if __name__ == "__main__":
    main()
    
