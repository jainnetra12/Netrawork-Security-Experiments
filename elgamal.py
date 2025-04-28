import random

def elgamal_encrypt(p, g, y, message):
    k = random.randint(1, p-2)
    a = pow(g, k, p)
    b = (pow(y, k, p) * message) % p
    return a, b

def elgamal_decrypt(p, x, a, b):
    s = pow(a, x, p)
    message = (b * pow(s, -1, p)) % p
    return message

p = int(input("Enter prime p: "))
g = int(input("Enter generator g: "))
x = int(input("Enter private key x: "))
message = int(input("Enter numeric message: "))
y = pow(g, x, p)
a, b = elgamal_encrypt(p, g, y, message)
print(f"Ciphertext (a,b): ({a}, {b})")

decrypted = elgamal_decrypt(p, x, a, b)
print("Decrypted Message:", decrypted)
