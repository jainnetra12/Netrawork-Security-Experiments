def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def multiplicative_inverse(e, phi):
    # Extended Euclidean Algorithm
    old_r, r = phi, e
    old_s, s = 1, 0
    old_t, t = 0, 1
    while r != 0:
        quotient = old_r // r
        old_r, r = r, old_r - quotient * r
        old_s, s = s, old_s - quotient * s
        old_t, t = t, old_t - quotient * t
    return old_t % phi

def encrypt(message, e, n):
    cipher = [(ord(char) ** e) % n for char in message]
    return cipher

def decrypt(cipher, d, n):
    message = ''.join([chr((char ** d) % n) for char in cipher])
    return message

# Main program
print("RSA Encryption and Decryption")
p = int(input("Enter first prime number (p): "))
q = int(input("Enter second prime number (q): "))

n = p * q
phi = (p-1)*(q-1)

e = int(input(f"Enter public key e (1 < e < {phi}) such that gcd(e, {phi}) = 1: "))
while gcd(e, phi) != 1:
    e = int(input(f"Invalid e. Enter e again: "))

d = multiplicative_inverse(e, phi)

print(f"Public Key: ({e}, {n})")
print(f"Private Key: ({d}, {n})")

message = input("Enter message to encrypt: ")
cipher_text = encrypt(message, e, n)
print("Encrypted Message:", cipher_text)

decrypted_message = decrypt(cipher_text, d, n)
print("Decrypted Message:", decrypted_message)
