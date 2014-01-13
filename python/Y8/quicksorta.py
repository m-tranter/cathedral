# quicksort.py   
# Tony Hoare 1960

def quicksort(array):
    """This function calls qsort() after setting the initial pivot."""
    left, right = 0, len(array) - 1
    initial_pivot(array,right)
    qsort(array,left,right)

def initial_pivot(numbs, i):
    """Sorts first, middle and last values. 
    Lowest becomes first, median becomes middle, highest becomes last."""
    mid = i // 2
    if numbs[0] > numbs[mid]:
        swap(numbs, 0, mid)
    if numbs[mid] > numbs[i]:
        swap(numbs, mid, i)
    if numbs[0] > numbs[mid]:
        swap(numbs, 0, mid)
    
def partition(array, left, right):
    """Partitions the list around the pivot."""
    # move middle term of array to end
    swap(array, right, (left + right) // 2)
    # use it as pivot
    pivot, lo, hi = array[right], left, right-1
    while lo <= hi:
        # one "finger" moves left from the right
        while array[hi] > pivot:
            hi -= 1
        # one "finger" moves right from the left
        while lo <= hi and array[lo] < pivot:
            lo += 1
        # only swap if lo & hi have not crossed
        if lo <= hi:
            swap(array, lo, hi)
            lo += 1
            hi -= 1
    swap(array,right,lo)
    return lo 

def swap(array, x, y):
    """Takes an array and two indices, swaps the values."""
    array[x], array[y] = array[y], array[x]

def qsort(array, left, right):
    """Recursively sort the list."""
    if left < right:
        p_ind_new =  partition(array, left, right)
        qsort(array, left, p_ind_new-1)
        qsort(array, p_ind_new+1, right)

