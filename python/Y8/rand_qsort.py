# rand_qsort.py Tony Hoare 1960
# uses a random pivot & 1 "finger"

from random import randint

def r_qsort(a, l = 0, r = None):
    """Recursively sort the list."""
    if r == None:
        r = len(a) - 1 
    if l < r:
        ind = partition(a, l, r)
        r_qsort(a, l, ind - 1)
        r_qsort(a, ind + 1, r)

def partition(a, l, r):
    """Partition function."""
    swap(a, l, randint(l+1, r))
    pivot, i = a[l], l
    for j in range(l + 1, r + 1):
        if a[j] <= pivot:
            i += 1
            swap(a, i, j)
    swap(a, l, i)
    return i

def swap(a, x, y):
    """Takes an array and two indices, swaps the values."""
    a[x], a[y] = a[y], a[x]

