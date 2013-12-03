# binary_search2.py
# a classic algorithm - version which returns the index.

def bSearch(x, my_list, l = 0, r = -1):
    """Searches a sorted list for x. Returns the index or -1"""
    if r == l:
        return -1
    elif r == -1:
        r = len(my_list) - 1
    n = (r + l) // 2
    mid = my_list[n]
    if mid == x:
        return n
    elif mid < x:
        return bSearch(x, my_list, n + 1, r)
    else:
        return bSearch(x, my_list, l, n)
