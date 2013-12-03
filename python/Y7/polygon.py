# polygon.py draws polygons
from turtle import *

def main():
    print ("*** Polygons ***")
    while 1:
        try:
            how_many = input("Number of sides: ")
            if how_many == 'q':
                return
            how_big = int(input("Length of sides: "))
            polygon(how_big, int(how_many))
        except ValueError:
            print("I only accept whole numbers.")

def polygon(length, sides):
    a = Turtle()
    a.pensize(2)
    for i in range(sides):
        a.fd(length)
        a.left(360/sides)

if __name__ == "__main__":
           main()
