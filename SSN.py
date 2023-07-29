import random
from prime import prime_field, prime_field_value, get_prime

class SSN():
    def __init__(self, secret:int, n:int, k:int):
        self.secret = secret
        self.n = n
        self.k = k
        self.p = get_prime(n)
        self.polynomial_coefficients = [secret] + [random.randint(0, self.p-1) for i in range(k-1)]

    def get_func_value(self, x:int) -> int:
        return sum([self.polynomial_coefficients[i] * (x ** i) for i in range(self.k)])
    
    def shares(self) -> dict:
        share_set = dict()
        for i in range(self.k):
            print(self.get_func_value(i))
            share_set[i] = prime_field_value(self.get_func_value(i), self.p)
        return share_set          



ssn = SSN(42, 5, 3)
print(ssn.polynomial_coefficients)
print(ssn.p)
print(ssn.shares())