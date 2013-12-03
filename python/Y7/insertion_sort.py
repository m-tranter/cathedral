# insertion_sort.py

def insertion(a):
    """Takes a list and sorts it using insertion sort."""
    for i in range(1, len(a)):
        val, j = a[i], i-1
        while j >= 0 and a[j] > val:
            a[j+1] = a[j]
            j -= 1
        a[j+1] = val
        print(a)
        
