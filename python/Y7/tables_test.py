# tables_test.py
# program to help user learn multiplication tables.

from random import shuffle

def main():
    print("*** Multiplication Table Practice ***")
    print("Enter 'q' to quit.")
    while 1:
        num = input("\nNumber to test (2-13): ")
        if num == 'q':
            return
        try:
            num = int(num)
            if num < 2 or num > 13:
                raise ValueError
            else:
                print("You scored {} out of 11.".format(doTest(num)))
        except ValueError:
            print("Please enter a number from 2 to 13.")
            
def doTest(n):
    """Takes a number and runs a test. Returns score."""
    score = 0
    my_list = list(range(2,13))
    shuffle(my_list)
    for i in my_list:
        if input("What is {0} times {1}? ".format(n, i)) == str(i*n):
            score += 1
            print("Correct.")
        else:
            print("Wrong.")
    return score

if __name__ == "__main__":
    main()

