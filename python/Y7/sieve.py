# sieve.py The Sieve of Eratosthenes

def main():
    print("*** Sieve of Eratosthenes ***")
    while 1:
        try:
            print(display(sieve([True] * (int(input("Numbers up to: ")) + 1))))
        except ValueError:
            print("Huh?")

def sieve(my_list):
    """Takes the list and sieves the indexes. Composite index values marked "False"."""
    # mark all even cells over 2 "False" 
    for i in range(4, len(my_list),2):
        my_list[i] = False
    # we only need to go as high as the square root of the highest number
    limit = int(len(my_list) ** 0.5) + 1
    for i in range(3, limit, 2):
        # if the number is still unchecked
        if my_list[i]:
            # uncheck all the multiples
            for j in range(i*i, len(my_list),2*i):
                my_list[j] = False
    return my_list

def display(array):
    """Returns a string made up of all the indices of elements marked True."""
    s, j = "\nPrimes:\n", 0
    p = len(str(len(array))) + 1
    # Using a slice to skip the first two elements in the list (zero and one).
    for (i, isPrime) in enumerate(array[2:], 2):
        if isPrime:
            s += str(i).rjust(p)
            j += 1
            if not j % 10:
                s += '\n'
    return s

if __name__ == "__main__":
    main()
