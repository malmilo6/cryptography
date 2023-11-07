from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
import hashlib
import random

# Given prime p and base g
p = 17
g = 2  # or any other primitive root modulo p

# Alice generates her private key a and computes her public value A
a = random.randint(2, p-2)
A = pow(g, a, p)

# Bob generates his private key b and computes his public value B
b = random.randint(2, p-2)
B = pow(g, b, p)

# Alice and Bob exchange their public values A and B

# Alice computes the shared secret with Bob's public value
s_alice = pow(B, a, p)

# Bob computes the shared secret with Alice's public value
s_bob = pow(A, b, p)

# Verify both shared secrets are equal (this step is not part of the algorithm, just for demonstration)
assert s_alice == s_bob

# Hash the shared secret to create a 256-bit AES key
aes_key = hashlib.sha256(str(s_alice).encode()).digest()

# Alice can now encrypt a message with the AES key
cipher = AES.new(aes_key, AES.MODE_CBC)
plaintext = "This is a secret message."
ciphertext = cipher.encrypt(pad(plaintext.encode(), AES.block_size))
iv = cipher.iv

# Send iv and ciphertext to Bob

# Bob can now decrypt the message with the AES key and iv
cipher = AES.new(aes_key, AES.MODE_CBC, iv)
decrypted_msg = unpad(cipher.decrypt(ciphertext), AES.block_size).decode()

# Verify the decrypted message is the same as the original
assert decrypted_msg == plaintext
