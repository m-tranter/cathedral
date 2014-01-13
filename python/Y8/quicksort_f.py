# functional_quicksort.py

def do_sort(l):
    """This wraps f_qsort to mimic an inline sort."""
    l[:] = f_qsort(l)
    
def f_qsort(a):
    """Takes a list of numbers and returns a sorted list."""
    l = len(a)
    if l <= 1:
        return a
    else:
        pivot = a[l // 2]
        less = f_qsort(list(filter(lambda x: x < pivot, a)))
        equal = list(filter(lambda x: x == pivot, a))
        more = f_qsort(list(filter(lambda x: x > pivot, a)))
        return less + equal + more
