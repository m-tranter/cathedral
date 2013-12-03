# hangman2.py
# with word-list saved to disc

from random import *

def main():
        print("*** Hangman ***")
        while 1:
                print("""
1. Play Game
2. Edit Word List
q. Quit\n""")
                ans = input("Your choice: ")
                if ans == 'q':
                        return
                elif ans == '1':
                        play()
                elif ans == '2':
                        editList()
                else:
                        print("Huh?")
                        
def play():
        """This runs the game itself."""
        # pick a word randomly
        word = choice(load())
        # abort if there are no words
        if not word:
                print("Couldn't find any words, please edit word-list.")
                return
        # continue to play a game    
        guessed, lWord = '', len(word)
        print("\nThe word is {0} letters long.\n{1}".format(lWord, "_ " * lWord))

        for i in range(5):
                letter = input("\nGuess a letter: ").lower()
                if len(letter) == 1:
                        if letter in word:
                                temp = "\nYes, the word contains "
                                guessed += letter
                        else:
                                temp = "\nNo, it doesn't contain "
                        output = ' '.join(x if x in guessed else '_' for x in word)
                        print("{0} '{1}'.\n{2}".format(temp, letter, output))
                else:
                        print("Just one letter for now please!")
                
        # user tries to guess word        
        print("\nThat's all your letter guesses used up.")
        if input("\nNow guess the word: ") == word:
                print("\nWell done, you got it!")
        else:
                print("\nSorry, wrong. It was: \"{}\".".format(word))

def load():
        """Attempt to load words from file."""
        # check to see if a list of words exists
        try:
                f = open("hangman.csv")
                words = f.read().split(',')
                f.close()
        except FileNotFoundError:
                words = [False]
        return words

def editList():
        """Edit a list of words."""
        words = load()
        # this is what we do if there are some words already
        if words[0]:
                print("You have {} word(s) in your list.".format(len(words)))
                if input("Do you want to remove any of them? ") == 'y':
                    print(''.join("{0}: {1}\n".format(i,w) for i, w in enumerate(words, 1)))
                    a = input("Numbers of the word(s) to remove, separated by commas: ").split(',')
                    try:
                        words = [x for x in words if x not in [words[int(y)-1] for y in a]]
                    except (ValueError, IndexError):
                        print("Invalid entry. Returning to main menu.")
                        return
        else:
                words = []
        print("Type in a word to add it to the list. Use Enter to quit.")
        while 1:
                word = input("Word: ").lower()
                if not word:
                        break
                else:
                        words.append(word)
        f = open("hangman.csv", 'w')
        f.write(','.join(words))
        f.close()
        print("New word-list written to file.")

if __name__ == "__main__":
        main()

