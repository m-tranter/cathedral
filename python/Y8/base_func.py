# base_func.py

# declare a constant
HEX = "0123456789ABCDEF"

def main():
    print("*** Positive Denary Integer to Another Base ***")
    print("Enter number and base (2-16), separated by a comma.")
    print("Use 'q' to quit.")
    while 1:
        a = input("n, b: ")
        if a == 'q':
            return
        else:
            try:
                # unpack the values
                n, b = [int(x) for x in a.split(',')]
                if not n:
                    print("0")
                elif n < 0 or b < 2 or b > 16:
                    raise ValueError
                else:
                    print("> {}".format(toBase(n,b)))
            except ValueError:
                print("Huh?")

def toBase(n, b):
    """Converts positive integer to another base."""
    if not n:
        return ''
    else:        
        d, m = divmod(n,b)
        return toBase(d, b) + HEX[m]
    
if __name__ == "__main__":
    main()
