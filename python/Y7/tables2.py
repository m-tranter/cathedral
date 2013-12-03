# tables2.py

print("*** Multiplication Tables ***")
print("Enter 'q' to quit.")
while True:
    num = input("\nEnter a number: ")
    # check to see if the user wants to quit.
    if num == 'q':
        break
    try:
        # if int(num) fails, the error gets caught by the "except:"
        num = int(num)
        for i in range(1, 14):
            # add an extra space for the numbers < 10.
            if i < 10:
                print(' ', end = '')
            print("{0} times {1} is {2}.".format(i, num, i*num))
    except ValueError:
        print("Please enter a whole number.")
