def rsa_encrypt(p, q, e, message):
    n = p * q
    cipher = [(ord(char) ** e) % n for char in message]
    return cipher

p = int(input("Enter prime p: "))
q = int(input("Enter prime q: "))
e = int(input("Enter public key e: "))
message = input("Enter message: ")
cipher_text = rsa_encrypt(p, q, e, message)
print("Encrypted Text:", cipher_text)
