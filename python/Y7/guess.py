# Number guessing game
# Generates a random number and asks the player to guess it.

import random

print("\tWelcome to 'Guess My Number'!")
print("\nI'm thinking of a number between 1 and 100.")
print("Try to guess it in as few goes as possible.")

# set the initial variables
the_number = random.randint(1,100)
guess = True
tries = 0

# guessing loop
while guess != the_number:
    guess = int(input("Take a guess:"))
    tries += 1
    if guess > the_number:
        print("Lower ...")
    elif guess < the_number:
        print("Higher ...")

print("You guessed it! The number was", the_number)
print("And you only took", tries, "tries.")

            
