# template.py

def main():
    print("*** Just a template! ***")
    while True:
        ans = input("Surprise me: ")
        if ans == 'q':
            return
        else:
            print(dummy(ans))

def dummy(x):
    """This function is trivial."""
    return "You entered: \"{}\".".format(x)

if __name__ == "__main__":
    main()
