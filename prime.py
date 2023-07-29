def prime_field(p) -> list:
    """Returns a finite field with p elements."""
    return list(range(p))

def prime_field_value(x, p) -> int:
    """Returns the value of x in the finite field with p elements."""
    return x % p

def get_prime(n) -> int:
    """Returns a prime greater than n and k"""
    p = n + 1
    while not is_prime(p):
        p += 1
    return p

def is_prime(n) -> bool:
    """Returns True if n is prime, False otherwise."""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i = i + 6
    return True

def prime_field_group(g, p) -> list:
    """Returns a finite field group with p elements."""
    return list(set([g ** i % p for i in range(p)]))

print(prime_field_group(3, 11))