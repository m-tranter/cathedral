# bubble_sort.py simple sorting function

def bubble(a):
    """Takes a list and sorts it."""
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


