import random
from sympy import mod_inverse

# Provided large prime p and generator g
p = 3231700607131100730015351347782516336248805713348907517458843413926980683413621000279205636264016468545855635793533081692882902308057347262537355474246124574102620252791657297286270630032526342821314576693141422365422094111134862999165747826803423055308634905063555771221918789033272956969696129743856241741236237225197346402691855797767976823014625397933058015226858730761197532436467475855460715043896844940366130497697812854295958659597567051283852132784468522925504568272879113720098931873959143374175837826000278034973198552060607533234122603254684088120031105907484281003994966956119696956248629032338072839127039
g = 2


# ElGamal key generator
def generate_keys():
    x = random.randrange(2, p - 1)  # Private key
    y = pow(g, x, p)  # Public key
    return x, y


# ElGamal encryption
def encrypt(y, msg):
    k = random.randrange(2, p - 1)
    a = pow(g, k, p)
    b = [(ord(char) * pow(y, k, p)) % p for char in msg]
    return a, b


# ElGamal decryption
def decrypt(x, a, b):
    s = pow(a, x, p)
    m = [chr((char * mod_inverse(s, p)) % p) for char in b]
    return ''.join(m)


# Main function
if __name__ == "__main__":
    print("ElGamal Encrypter/ Decrypter")

    # Key generation
    private_key, public_key = generate_keys()
    print(f"Public Key: {public_key}")
    print(f"Private Key: {private_key}")

    # Get the message to encrypt
    message = input("Enter a message to encrypt: ")

    # Encrypt the message
    a, encrypted_msg = encrypt(public_key, message)
    print("Encrypted Message:")
    print(' '.join(map(lambda x: str(x), encrypted_msg)))

    # Decrypt the message
    decrypted_msg = decrypt(private_key, a, encrypted_msg)
    print("Decrypted Message:")
    print(decrypted_msg)
