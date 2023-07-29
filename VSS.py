from SSS import SSS

class VSS(SSS):
    def __init__(self, secret, n, k, g):
        super().__init__(secret, n, k)
        self.g = g

    def commitments(self):
        commitment = list()
        for i in range(self.k):
            commitment.append((self.g ** self.polynomial_coefficients[i]) % self.p)
        return commitment
    
    def validate(self, key:int, value:int) -> bool:
        commitments = self.commitments()
        val_value = (self.g ** self.get_func_value(key)) % self.p   
        product = 1
        for i,j in enumerate(commitments):
            product *= (j ** (key**i))%self.p
        print(val_value, product%self.p)
        return val_value == product%self.p
        

if __name__ == "__main__":
    vss = VSS(42, 5, 3, 2)
    shares = vss.shares()
    print(vss.polynomial_coefficients)
    print(shares)
    print(vss.commitments())
    print(vss.reconstruct(shares))
    
    print(vss.validate(1, shares[1]))
    print(vss.validate(2, 1234))
    print(vss.validate(3, 1234))
    print(vss.validate(4, shares[4]))

    