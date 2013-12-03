# fib_test.py
# includes the iterative and recursive functions

from time import *

def fibr(n):
    if n < 2:
        return n
    else:
        return fibr(n-1) + fibr(n-2)

def fibi(x):
    a, b = 0, 1
    for i in range(x-1):
        b = a + b
        a = b - a 
    return b

for n in [35, 40]:
    for f in [fibi, fibr]:
        t = time()
        a = f(n)
        t = time() - t
        print("{0}: {1} secs.\nfib({2}) = {3}".format(f.__name__, str(round(t,4)).rjust(7), n, a))
