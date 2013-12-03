# try.py

while 1:
    try:
        num = int(input("Please enter a whole number: "))
        print("Thanks, you entered {}.".format(num))
    except ValueError:
        print("You suck!")
