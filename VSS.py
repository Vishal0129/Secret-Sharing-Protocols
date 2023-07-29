from get_data_vss import get_data

def mod_inverse(a, m):
    m0 = m
    t, q = 0, 0
    x0, x1 = 0, 1

    if m == 1:
        return 0

    while a > 1:
        q = a // m
        t = m
        m = a % m
        a = t
        t = x0
        x0 = x1 - q * x0
        x1 = t

    if x1 < 0:
        x1 += m0

    return x1

def field_prime_value(num, p):
    return num % p



if __name__ == "__main__":
    url_valid = 'https://hash-effect.onrender.com/vss/share/valid'
    url_invalid = 'https://hash-effect.onrender.com/vss/share/invalid'

    index, value, commitments, g, p, p1 = get_data(url_valid).values()

    is_valid = validate(index, value, commitments, g, p, p1)
    print("Is Valid:", is_valid)
