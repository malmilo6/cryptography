from sympy import randprime, isprime, gcd, mod_inverse


# Euclid's extended algorithm for finding the multiplicative inverse of two numbers
def multiplicative_inverse(e, phi):
    return mod_inverse(e, phi)


# Test if a number is prime using sympy's isprime
def is_prime(num):
    return isprime(num)


# Generate keypair with sympy's randprime function to generate large prime numbers
def generate_keypair(bitsize):
    p = randprime(2 ** (bitsize // 2), 2 ** ((bitsize // 2) + 1))
    q = randprime(2 ** (bitsize // 2), 2 ** ((bitsize // 2) + 1))
    while q == p:
        q = randprime(2 ** (bitsize // 2), 2 ** ((bitsize // 2) + 1))

    n = p * q
    phi = (p - 1) * (q - 1)

    # An integer e such that e and phi(n) are coprime
    e = 65537  # It's common to use 65537 as a public exponent in RSA

    # Check if e and phi(n) are coprime
    if gcd(e, phi) == 1:
        # Use Extended Euclid's Algorithm to generate the private key
        d = multiplicative_inverse(e, phi)
    else:
        raise Exception("e and phi are not coprime, which shouldn't happen with e=65537.")

    return (e, n), (d, n)


def encrypt(pk, plaintext):
    key, n = pk
    cipher = [pow(ord(char), key, n) for char in plaintext]
    return cipher


def decrypt(pk, ciphertext):
    key, n = pk
    plain = [chr(pow(char, key, n)) for char in ciphertext]
    return ''.join(plain)


if __name__ == '__main__':
    print("RSA Encrypter/Decrypter")
    bitsize = int(input("Enter the bit size for the prime numbers (256, 512, 1024, etc): "))
    public, private = generate_keypair(bitsize)
    print("Your public key is ", public, " and your private key is ", private)
    message = input("Enter a message to encrypt with your public key: ")
    encrypted_msg = encrypt(public, message)
    print("Your encrypted message is: ")
    print(' '.join(map(lambda x: str(x), encrypted_msg)))
    print("Decrypting message with private key ", private, " . . .")
    decrypted_msg = decrypt(private, encrypted_msg)
    print("Your message is:")
    print(decrypted_msg)
