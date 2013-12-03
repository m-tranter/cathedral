# star.py

from turtle import *

def main():
    """Draws a star."""
    pen = Turtle(visible = False)
    pen.speed(30)
    pen.pensize(3)
    pen.color('blue', 'magenta')
    pen.begin_fill()
    while 1:
        pen.fd(200)
        pen.lt(100)
        if abs(pen.pos()) < 1:
            break
    pen.end_fill()

if __name__ == "__main__":
    main()
