# hangman.py - simple hangman game

from random import *

def main():
        WORDS = ['acorn', 'apple', 'apricot', 'grape', 'grapefruit',
         'kiwi', 'lemon', 'mango', 'melon', 'orange', 'peach',
         'pear', 'pineapple', 'raspberry', 'satsuma']
        
        # pick a word randomly
        word = choice(WORDS)
        guessed, lWord = '', len(word)
        
        print("*** Hangman ***")
        print("\nThe word is {} letters long.".format(lWord))
        print("_ " * lWord)

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
                        
        print("\nThat's all your letter guesses used up.")
        if input("\nNow guess the word: ") == word:
                print("\nWell done, you got it.")
        else:
                print("\nSorry, wrong. It was: \"{}\".".format(word))

if __name__ == "__main__":
        main()

