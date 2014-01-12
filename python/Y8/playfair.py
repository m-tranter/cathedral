# playfair.py
# Implementation of Playfair Cipher as described in "Codes and Ciphers" by Robert Churchhouse. 

def main():
    print("*** The Playfair Cipher ***")
    print("Note: The letter 'J' may not be used in this version of the Playfair cipher.")
    while 1:
        keyword = input("Please enter a keyword: ").upper()
        if keyword.isalpha():
            break
        else:
            print("The keyword must contain letters only.")
    table = makeGrid(keyword)
    # take the message and prepare it for encryption
    msg = ''.join(x for x in input("Please enter your message: ").upper() if x.isalpha() and x != 'J')
    if input("Enter 'd' to decipher, anything else to encipher: ") == 'd':
        print("Here is the deciphered text:\n" + playfair(msg, table, -1))
        print("Note: some 'Q's may have been introduced as padding.")
    else:
        print("Here is the enciphered text:\n" + cipherWords(playfair(msg, table)))

def makeGrid(keyword):
    """Use the keyword to construct the playfair table."""
    key = ''.join(x for i,x in enumerate(keyword) if x not in keyword[:i] and x != 'J')
    alpha = key + ''.join(x for x in "ABCDEFGHIKLMNOPQRSTUVWXYZ" if x not in key)
    playfair = []
    for i in range(0,25,5):
        playfair.append(alpha[i:i+5])
    return playfair

def playfair(msg, table, shift = 1):
    """Takes the text and the table and returns enciphered text."""
    cipher, i = '', 0
    # the while loop carves the message up into digraphs
    while i < len(msg):
        digraphA = msg[i]
        i += 1
        try:
            digraphB = msg[i]
            if digraphA == digraphB:
                digraphB= 'Q'
            else:
                i += 1
        except IndexError:
            digraphB = 'Q'
        # encipher the digraph
        rowA, colA = getPos(digraphA, table)
        rowB, colB = getPos(digraphB, table)
        if rowA == rowB:
            cipher += table[rowA][(colA+shift)%5] + table[rowB][(colB+shift)%5]
        elif colA == colB:
            cipher += table[(rowA+shift)%5][colA] + table[(rowB+shift)%5][colB]
        else:
            cipher += table[rowA][colB] + table[rowB][colA]
    return cipher

def getPos(ch, table):
    """Takes a letter and the table and returns the position (row, col)."""
    for i, row in enumerate(table):
        try:
            return (i, row.index(ch))
        except ValueError:
            pass

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
      
if __name__ == "__main__":
    main()
    
    
    
