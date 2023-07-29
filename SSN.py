import random
from prime import prime_field, prime_field_value, get_prime
class SSN(random.random):
    def __init__(self, secret:int, n:int, k:int):
        self.secret = secret
        self.n = n
        self.k = k
        self.p = get_prime(n)
        self.polynomial_coefficients = [random.randint(0, self.p-1) for i in range(k)]

    def get_func_value(self, x:int) -> int:
        return sum([self.polynomial_coefficients[i] * (x ** i) for i in range(self.k)])
    
    def shares(self) -> dict:
        share_set = dict()
        for i in range(self.k):
            share_set[i] = (i, self.get_func_value(i))
        return share_set            




print(SSN(1, 2, 3).polynomial_coefficients)