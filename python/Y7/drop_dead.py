# drop_dead.py  - simple dice game

from random import *

def main():
    print("*** Drop Dead ***\n")
    while 1:
        score, lives = 0, 5
        while lives:
            temp = 0
            dice = [randint(1,6) for x in range(lives)]
            fivesAndTwos = dice.count(5) + dice.count(2)
            if not fivesAndTwos:
                temp = sum(dice)
                score += temp
            else:
                lives -= fivesAndTwos
            input("{0}\nThis round: {1}\nScore = {2}".format(dice, temp, score))
        print("All dice gone! You scored: {}.".format(score))
        if input("Play again? ") == 'n':
            return

if __name__ == "__main__":
    main()
