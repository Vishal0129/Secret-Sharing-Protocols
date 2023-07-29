import random
from utils import prime_field_value, get_prime, mod_inverse

class SSS():
    def __init__(self, secret:int, n:int, k:int):
        self.secret = secret
        self.n = n
        self.k = k
        self.p = get_prime(self.secret)
        self.polynomial_coefficients = [secret] + [random.randint(0, self.p-1) for i in range(k-1)]

    def get_func_value(self, x: int) -> int:
        return sum([self.polynomial_coefficients[i] * (x ** i) for i in range(self.k)])
    
    def shares(self) -> dict:
        share_set = dict()
        for i in range(self.k):
            print(self.get_func_value(i+1))
            share_set[i+1] = prime_field_value(self.get_func_value(i+1), self.p)
        return share_set          

    
    
    def reconstruct(self, shares: dict) -> int:
        if len(shares) < self.k:
            print("Secret cannot be reconstructed")
            return None
        s = 0
        for i in shares.keys():
            numerator = 1
            denominator = 1
            for j in shares.keys():
                if i != j:
                    numerator *= -j
                    denominator *= i - j
            if denominator == 0:
                continue
            s += shares[i] * numerator * mod_inverse(denominator, self.p)
        return prime_field_value(s, self.p)
