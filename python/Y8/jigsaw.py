# jigsaw.py
# based on description in "Codes and Ciphers" by R. F. Churchhouse

from math import ceil

def main():
    print("*** Jigsaw Cipher ***")
    print("First I need a keyword. I will convert this into a column-key.")
    print("For instance 'ZEBRAS' would become 6,3,2,4,1,5.")
    key = False
    while not key:
        temp = input("Enter a keyword. Repeated letters will be ignored: ")
        if temp.isalpha():
            key = getKey(temp.upper())
        else:
            print("Please try again.")
            
    nice = ','.join(str(x) for x in key)
    print("Here is the column-key generated from your word: {}.".format(nice))
    print("Enter your text. Non-alphabetical characters will be stripped.")
    # get the text as upper case letters only.
    msg = ''.join(x for x in input("Text: ") if x.isalpha()).upper()
    if input("Enter 'd' to decipher, anything else to encipher: ") == 'd':
        print(decipher(msg, key))
    else:
        print(cipherWords(encipher(msg,key)))

def encipher(msg,key):
    """Takes the message & the key and returns the enciphered message."""
    # set up the table
    lKey, lMsg = len(key), len(msg)
    table, cipher = [], ''
    for i in range(0, lMsg, lKey):
        try:
            table.append(msg[i:i + lKey])
        except IndexError:
            table.append(msg[i:])
    # encipher
    for y in [key.index(x + 1) for x in range(lKey)]:
        cipher += ''.join(row[y] for row in table if y < len(row))
    return cipher
    
def decipher(msg, key):
    """Takes the message and the key and prints
    the deciphered message."""
    lKey, lMsg = len(key), len(msg)
    rows = ceil(lMsg / lKey)
    fullCols = lKey - (rows * lKey - lMsg)
    table, count = [''] * lKey, 0
    # reassemble the table
    for ind in [key.index(x + 1) for x in range(lKey)]:
        end = count + rows
        if ind >= fullCols:
            end -= 1
        table[ind] = msg[count: end]
        count = end
    # read off the original message
    new = ''
    for i in range(rows):
        for j in range(lKey):
            try:
                new += table[j][i]
            except IndexError:
                break
    return new

def getKey(s):
    """Takes a string and returns the keys as a list of ints."""
    keys = [ord(x) for i, x in enumerate(s) if x not in s[:i]]
    for j in range(len(keys), 0, -1):
        keys[keys.index(max(keys))] = j
    return keys

def cipherWords(text):
    """Prepares the cipher in lines of 5-letter
    cipher words for printing."""
    msg = text[0]
    for i, letter in enumerate(text[1:],1):
        if i % 25 == 0:
            msg += '\n'
        elif i % 5 == 0:
            msg += ' '
        msg += letter
    return msg
            
if __name__  == "__main__":
    main()
