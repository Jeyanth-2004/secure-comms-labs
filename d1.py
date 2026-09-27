primes = [2, 3]
k = 1
while 6 * k - 1 <= 100:
    for c in (6 * k - 1, 6 * k + 1):
        if c <= 100 and all(c % p != 0 for p in primes if p * p <= c):
            primes.append(c)
    k += 1
print("Primes up to 100:", primes)
