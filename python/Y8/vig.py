# vig.py
# very simple Vigenere cipher program

def main():
    base = ord('A')
    print("*** Vigenere Cipher ***\n")
    keyGen = vig(getKey(base))
    action = 1
    if input("Enter 'd' to decipher, anything else to encipher: ") == 'd':
        action = -1
    # take the message and prepare it for encryption
    msg = ''.join(x for x in input("Please enter your message: ") if x.isalpha()).upper()
    print("Here is your text, prepared for encryption:\n" + msg)
    # perform the encryption
    cipher = ''.join(chr(base + (ord(x) - base + action * next(keyGen)) % 26) for x in msg)
    # display in cipher "words"
    if action == 1:
        print("Here is the enciphered message:\n" + cipherWords(cipher))
    else:
        print("Here is the deciphered message:\n" + cipher)

def cipherWords(text):
    """Prepares output. Lines of five five-letter "words"."""
    msg = text[0]
    for i, letter in enumerate(text[1:],1):
        if i % 25 == 0:
            msg += '\n'
        elif i % 5 == 0:
            msg += ' '
        msg += letter
    return msg

 Mdef vig(numbers):
    """Generator for the numbers in the keyword."""
    while 1:
        for i in numbers:
            yield i

def getKey(base):
    """This function takes the keyword and returns a list of shifts."""
    while 1:
        key = input("Please enter a key: ").upper()
        if key.isalpha():
            return [ord(x) - base for x in key]
        else:
            print("Please try again.")

if __name__ == "__main__":
    main()
