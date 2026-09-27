def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
def cipher(m, e, p):
    if not is_prime(p):
        return str(p) + " is not prime"
    return (m ** e) % p
print("8^5 mod 269 =", cipher(8, 5, 269))
print("8^5 mod 268 =", cipher(8, 5, 268))
