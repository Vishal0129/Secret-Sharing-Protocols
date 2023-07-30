# import random
# from cryptography.hazmat.backends import default_backend
# from cryptography.hazmat.primitives.asymmetric import rsa
# from cryptography.hazmat.primitives import serialization
# import hashlib

# data = dict(
#     {"group":{"generator":{"tag":"prime","data":{"value":"2","prime":"f81da59aa27c179f"}},"p":"7c0ed2cd513e0bcf"},"hash":{"value":"600763bca5936e86","prime":"7c0ed2cd513e0bcf"},"message":"Hash Effect!!!","publicKey":{"tag":"prime","data":{"value":"95073b6e87714370","prime":"f81da59aa27c179f"}},"signature":{"r":{"tag":"prime","data":{"value":"4cc830ddaf370137","prime":"f81da59aa27c179f"}},"sigma":{"value":"26ca77a6cdf821d5","prime":"7c0ed2cd513e0bcf"}}}
# )

primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307]

# def set_values():
#      private_key = random.choice(primes)
#      generator = random.choice(primes[:primes.index(private_key)])
#      public_key = pow(generator, private_key, primes[-1])
#      prime = random.choice(primes)
#      p = random.choice(primes)
#      k = random.choice(primes[:primes.index(p)])
#      return private_key, generator, public_key, prime, p, k

# private_key, generator, public_key, prime, p, k = set_values()
# print(private_key, generator, public_key, prime)

# message = input("Enter a message: ")
# message_hash = 0
# def encrypt_message(message, private_key, generator, prime, p):
#     # Generate a random number (z)
#     z = random.choice(primes)

#     # Calculate the random point R = z * G (mod prime)
#     R = (pow(generator, z, prime), pow(generator, z, p))

#     # Calculate the hash of the message
#     message_hash = int(hashlib.sha256(message.encode()).hexdigest(), 16)

#     # Calculate the encryption factors
#     s = (message_hash + private_key * R[0]) % prime
#     v = (R[0] - s * generator) % prime

#     # Return the encrypted message (R, s, v)
#     return R, s, v

# R, s, v = encrypt_message(message, private_key, generator, prime, p)
# print(R, s, v)

# r = pow(generator, k)
# print(k)

# mu = message_hash * private_key + k
# print(mu)

# data['group']['generator']['data']['value'] = str(hex(generator))
# data['group']['generator']['data']['prime'] = str(hex(prime))
# data['group']['p'] = str(hex(p))
# data['hash']['value'] = str(hex(message_hash))
# data['hash']['prime'] = str(hex(prime))
# data['message'] = message
# data['publicKey']['data']['value'] = str(hex(public_key))
# data['publicKey']['data']['prime'] = str(hex(prime))
# data['signature']['r']['data']['value'] = str(hex(R[0]))
# data['signature']['r']['data']['prime'] = str(hex(prime))
# data['signature']['sigma']['value'] = str(hex(mu))
# data['signature']['sigma']['prime'] = str(hex(prime))



# print(data)
import json
import random
import hashlib
import requests

# The list of primes you provided
# primes = [2, 3, 5, 7, 11, 13, ...]

def set_values():
    private_key = random.choice(primes)

    # Loop until a different generator is found
    generator = random.choice(primes[:primes.index(private_key)])
    public_key = pow(generator, private_key, primes[-1])

    prime = random.choice(primes)
    p = random.choice(primes)
    return private_key, generator, public_key, prime, p

def get_small_hash(message):
    full_hash = hashlib.sha256(message.encode()).hexdigest()
    small_hash = full_hash[:8]  # Take the first 8 characters of the hash
    return int(small_hash, 16)

def encrypt_message(message, private_key, generator, prime, p):
    # Generate a random number (z)
    z = random.choice(primes)

    # Calculate the random point R = z * G (mod prime)
    R = (pow(generator, z, prime), pow(generator, z, p))

    # Calculate the hash of the message (small hex value)
    message_hash = get_small_hash(message)

    # Calculate the encryption factors
    s = (message_hash + private_key * R[0]) % prime
    v = (R[0] - s * generator) % prime

    # Return the encrypted message (R, s, v)
    return R, s, v

def main():
    private_key, generator, public_key, prime, p = set_values()
    message = input("Enter a message: ")

    # Encrypt the message
    R, s, v = encrypt_message(message, private_key, generator, prime, p)
    r = pow(generator, k)

    # Fill in the values of the API request body
    api_body = {
        "group": {
            "generator": {
                "tag": "prime",
                "data": {
                    "value": str(hex(generator)),
                    "prime": str(hex(prime))
                }
            },
            "p": str(p)
        },
        "hash": {
            "value": hashlib.sha256(message.encode()).hexdigest(),
            "prime": str(hex(prime))
        },
        "message": message,
        "publicKey": {
            "tag": "prime",
            "data": {
                "value": str(hex(public_key)),
                "prime": str(hex(prime))
            }
        },
        "signature": {
            "r": {
                "tag": "prime",
                "data": {
                    "value": str(hex(r)),
                    "prime": str(hex(prime))
                }
            },
            "sigma": {
                "value": str(hex(s)),
                "prime": str(hex(prime))
            }
        }
    }

    # Print the API request body
    print(json.dumps(api_body, indent=4))

    # Make the API request
    url = "https://hash-effect.onrender.com/schnorr/verify"
    response = requests.post(url, json=api_body)

    # Check if the signature is valid
    if response.status_code == 200:
        print("Signature is valid.")
    else:
        print("Signature is invalid.")

if __name__ == "__main__":
    main()
