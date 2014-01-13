# quicksort.py   
# Tony Hoare 1960

def qsort(array, left = 0, right = None):
    """Recursively sort the list."""
    if right == None:
        right = len(array) - 1
    if left < right:
        p_ind_new =  partition(array, left, right)
        qsort(array, left, p_ind_new-1)
        qsort(array, p_ind_new+1, right)
    
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



