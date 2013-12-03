# p_gen.py

def primes():
    """Generates primes."""
    yield 2
    p, n = [2], 3
    while 1:
        if not len([x for x in p if not n % x]):
            p.append(n)
            yield n
        n += 2

