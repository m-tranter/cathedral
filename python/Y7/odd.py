# odd.py

def odd(n):
    """Tests to see if n is odd, even or zero."""
    if not n:
        print("Zero.")
    elif not n%2:
        print("Even.")
    else:
        print("Odd.")
