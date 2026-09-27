import sys
def factors(n):
    f = []
    d = 2
    while d * d <= n:
        while n % d == 0:
            f.append(d)
            n //= d
        d += 1
    if n > 1:
        f.append(n)
    return f
n = int(sys.argv[1]) if len(sys.argv) > 1 else 432
print(n, "->", factors(n))
