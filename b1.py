def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a
print("B.1 gcd(4105,10) =", gcd(4105, 10))
print("B.1 gcd(4539,6) =", gcd(4539, 6))
for a, b in [(5435, 634), (5432, 634)]:
    print("B.2", a, b, "gcd =", gcd(a, b), "co-prime:", gcd(a, b) == 1)
