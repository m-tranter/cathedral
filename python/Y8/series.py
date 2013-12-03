# series.py
# Program to generate simple polynomial number sequences.

def main():
    print("*** Series ***\nPlease use this format: 'x2 + 3x - 6'.")
    print("Enter 'q' to quit.")
    while 1:
        ans = input("\nEnter function: ").replace(' ', '')
        if ans == 'q':
            return
        fun = getProc(ans)
        if not fun:
            print("Could not parse function.")
            continue
        try:
            a,b = input("Range separated by a comma (default = 1,10): ").split(',')
            print(output(fun, int(a), int(b)+1))
        except ValueError:
           print(output(fun))

def output(fun, a = 1, b = 11):
    """Prepares printable output."""
    n = list(range(a,b))
    fn = [fun(x) for x in n]
    l = [max(len(str(a)),len(str(b)))+1 for a, b in zip(n,fn)]
    fmt = ''.join("{{{0}:>{1}}}".format(i, z) for i, z in enumerate(l))
    s = [''.join(fmt.format(*x)) for x in [n,fn]]
    return "   n: {0}\nf(n): {1}".format(s[0], s[1]) 

def getProc(fun):
    """Parses input from user. Returns a procedure to calculate f(n)."""
    terms = []
    for term in [x for x in fun.replace('-', "+-").split('+') if x]:
        if 'x' not in term:
            term = term + "x0"
        if term[0] == 'x':
            term = '1'+ term
        if term[:2] == '-x':
            term = "-1" + term[1:]
        if term[-1] == 'x':
            term += '1'
        try:
            p, q = term.split('x')
            terms.append((float(p), float(q)))
        except ValueError:
            return False
   
    # make a procedure from the list of terms.
    return lambda x: tryInt(sum(list(p * x ** q for p,q in terms)))

def tryInt(n):
    """Takes a float and returns an int if possible."""
    if not n%1:
        n = int(n)
    return n

if __name__ == "__main__":
    main()
