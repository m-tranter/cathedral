# caesar.py
# very simple Caesar cipher program

def main():
    print("*** Caesar Cipher ***\n")
    base = ord('A')
    shift = getNum()
    action = input("Enter 'd' to decipher, anything else to encipher: ")
    if action == 'd':
        shift = -shift
    # take the message and prepare it for encryption
    msg = ''.join(x for x in input("Please enter your message: ") if x.isalpha()).upper()
    print("Here is your message, prepared for encryption:\n" + msg)
    # perform the encryption
    cipher = ''.join(chr(base + (ord(x) - base + shift) % 26) for x in msg)
    # display in cipher "words"
    if action != 'd':
        print("Here is the enciphered message:\n" + cipherWords(cipher))
    else:
        print("Here is the deciphered message:\n" + cipher)
    
def cipherWords(text):
    """Prepares the cipher in lines of 5-letter cipher words for printing."""
    msg = text[0]
    for i, letter in enumerate(text[1:],1):
        if i % 25 == 0:
            msg += '\n'
        elif i % 5 == 0:
            msg += ' '
        msg += letter
    return msg

def getNum():
    """This function makes sure a valid shift is given."""
    while 1:
        try:
            ans = int(input("Please enter a number from -26 to 26: "))
            if ans < -26 or ans > 26:
                raise ValueError
            else:
                return ans
        except ValueError:
            print("Please try again.")

if __name__ == "__main__":
    main()
