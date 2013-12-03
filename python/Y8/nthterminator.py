# nthterminator.py number series analyser.

from math import factorial as fact

def main():
    print("*** Nth-term-inator ***")
    #print("\nEnter a series of numbers separated by commas.")
    #print("To quit, type 'q' and press 'Enter'.")
    while 1:
        series = input("\nSeries: ")
        if series == 'q':
            return
        try:
            series = [float(x) for x in series.split(',')]
            print(analyse(series, series, []))
        except ValueError:
            print("Huh?")

def analyse(sLast, s, terms, power=0):
    """Recursive function to analyse the series."""
    # we are done if s is all zeros
    if set(s) == {0}:
        return prettyTerms(terms)
    # differences have not converged yet
    elif len(s) > 1 and not len(set(s)) == 1:
        return analyse(sLast, difference(s), terms, power + 1)
    # differences have converged
    elif len(set(s)) == 1 and not (terms and terms[-1][1] == power):
        coeff = s[0]/fact(power)
        terms.append((coeff,power))
        s = [x - coeff * i ** power for i, x in enumerate(sLast,1)]
        return analyse(s, s, terms)
    # failure
    else:
        return "Failed to analyse sequence."
    
def difference(s):
    """Takes a list of numbers and returns a list of differences."""
    return [s[i+1] - x for i, x in enumerate(s[:-1])]

def term(coeff, power):
    """Takes a 'difference' and the power of x.
    Returns corresponding term as a string."""
    # constant
    if not power:
        return tryInt(coeff)
    # n
    if coeff == 1:
        temp = 'n'
    elif coeff == -1:
        temp = '-n'
    else:
        temp = tryInt(coeff) + 'n'
    # n squared or higher
    if power == 1:
        return temp
    else:
        return temp + '^' + tryInt(power)
    
def tryInt(n):
    """Takes a float and returns best string representation."""
    if not n%1:
        n = int(n)
    return str(n)

def prettyTerms(t):
    """Takes a list of terms and turns it into a string."""
    if not t:
        return "f(n) = 0"
    t = [term(x,y) for x,y in t]
    s = ''.join(' - ' + x[1:] if x[0] == '-' else ' + ' + x for x in t[1:])
    return "f(n) = " + t[0] + s

if __name__ == "__main__":
    main()
