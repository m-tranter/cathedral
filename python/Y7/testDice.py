# die_test.py

from random import *

def main():
    print("*** Die Test ***")
    print("Answer the first question with 'q' to quit.")
    while 1:
        sides = input("\nHow many sides? ")
        if sides == 'q':
            return
        try:
            sides = int(sides)
            rolls = int(input("How many rolls? "))
            print(pretty(testDie(sides, rolls)))
        except ValueError:
            print("Huh?")

def pretty(a):
    """Sets the results out a bit more clearly."""
    string = "Results:"
    for i, n in enumerate(a, 1):
        string += "\n{0}: {1}.".format(i,n)
    return string

def testDie(s, r):
    """Runs a simulation of r rolls of an s sided die."""
    results = [0] * s
    for i in range(r):
        results[randrange(s)] += 1
    return results

if __name__ == "__main__":
    main()
