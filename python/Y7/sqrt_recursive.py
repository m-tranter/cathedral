# sqrt_r.py - finding square roots

# you can write this as "1e-12" if you like.
ERROR = 0.000000000001

def sqrt(x, g = 1):
    """Recursive version."""
    if abs(g*g - x) < ERROR:
        return g
    else:
        return sqrt(x, (g + x / g) / 2)
 
