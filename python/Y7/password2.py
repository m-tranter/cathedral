# password.py
# set a password and rate it.

def main():
    strength =[False, "weak.", "medium.", "strong."]
    print("""
*** Set your password ***
Password must be 6 to 12 characters.
You may use:
    numbers,
    upper-case letters,
    lower-case letters.
    """)
    while 1:
        p = input("\nEnter password: ")
        if len(p) < 6 or len(p) > 12:
            print("Password must be 6 to 12 characters.")
        elif input("Re-enter password: ") != p:
            print("Passwords did not match. Please try again.")
        else:
            s = howGood(p)
            if not s:
                print("Invalid character detected. Please try again.")
            else:
                print("Password set, strength: {}".format(strength[s]))
                break

def howGood(pwd):
    """Returns a number saying how good the password is."""
    u = l = d = 0
    for ch in pwd:
        if ch.isupper():
            u = 1
        elif ch.islower():
            l = 1
        elif ch.isdigit():
            d = 1
        else:
            return 0
    return u + l + d

if __name__ == "__main__":
    main()
