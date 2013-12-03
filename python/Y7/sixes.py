# sixes.py

from random import *

def main():
    print("*** Double Six ***")
    while 1:
        a = input("Player One: ")
        b = input("Player Two: ")
        winner = playGame(a,b)
        if winner == "draw":
            ans = input("It was a draw. Enter 'y' to continue.")
            if ans != y:
                return
        else:
            print("The winner was {}.".format(winner))
            return

def playGame(a,b):
    winner = False
    while not winner:
        dice = [0]*4
        for i in range(4):
            dice[i] = randint(1,6)
        for x,y,z in [(a, dice[0], dice[1]), (b, dice[2], dice[3])]:
            print("{0} rolled {1} and {2}.".format(x,y,z))
        input()
        if dice[0] == 6 and dice[1] == 6:
            winner = a
        if dice[2] == 6 and dice[3] == 6:
            if not winner:
                winner = b
            else:
                winner = "draw"
    return winner
        

if __name__ == "__main__":
    main()
