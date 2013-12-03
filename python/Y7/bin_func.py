# bin_func.py

def main():
    print("*** Positive Integer to Binary ***")
    print("Use 'q' to quit.")
    while 1:
        a = input("n: ")
        if a == 'q':
            return
        else:
            try:
                a = int(a)
                if a < 0:
                    raise ValueError
                elif not a:
                    print("0")
                else:
                    print("> {}".format(toBin(a)))
            except ValueError:
                print("Huh?")
            
def toBin(n):
    """Recursive function. Converts positive integer to binary."""
    if not n:
        return ''
    else:        
        d, m = divmod(n,2)
        return toBin(d) + str(m)
    
if __name__ == "__main__":
    main()
