# test_sort.py
from random import *
from time import *

def main():
    print("*** Bubble Sort vs. Insertion Sort ***")
    for y in [2000, 4000, 8000]:
        print("\nArray of {} random numbers from 0 to 999:".format(y))
        a = [randint(1,999) for x in range(y)]
        b = a[:]
        tic = time()
        insertion(a)
        toc = time()
        print("Insertion Sort: {} seconds.".format(str(round(toc-tic,1)).rjust(5)))
        tic = time()
        bubble(b)
        toc = time()
        print("Bubble Sort:    {} seconds.".format(str(round(toc-tic,1)).rjust(5)))
        
def insertion(a):
    """Takes an array and sorts it in place. Insertion sort."""
    for i in range(1, len(a)):
        val, j = a[i], i-1
        while j >= 0 and a[j] > val:
            a[j+1] = a[j]
            j -= 1
        a[j+1] = val

def bubble(a):
    """Takes an array and sorts it in place. Bubble Sort."""
    j = len(a)
    while True:
        swap = False
        j -= 1
        for k in range(j):
            if a[k] > a[k+1]:
                a[k], a[k+1] = a[k+1], a[k]
                swap = True
        # if we made no swaps on a pass, the list is sorted
        if not swap:
            return

if __name__ == "__main__":
    main()
    
