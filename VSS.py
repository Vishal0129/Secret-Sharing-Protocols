from SSN import SSS

class VSS(SSS):
    def __init__(self, secret, n, k):
        super().__init__(secret, n, k)

    def commitments(self, g):
        shares = super().shares()
        commitment = dict()
        for i in range(self.k):
            commitment[i] = g ** self.polynomial_coefficients[i] % self.p
        return commitment
    
    def validate(self, shares):
        pass
    