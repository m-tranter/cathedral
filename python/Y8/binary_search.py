# binary_search.py
# a classic algorithm

def bSearch(x, my_list):
    """Searches a sorted list for x. Returns True or False."""
    if not my_list:
        return False
    i = len(my_list) // 2 -1
    mid = my_list[i]
    if mid == x:
        return True
    elif mid < x:
        return bSearch(x, my_list[i+1:])
    else:
        return bSearch(x, my_list[:i])
