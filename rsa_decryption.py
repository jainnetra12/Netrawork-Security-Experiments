def rsa_decrypt(p, q, e, cipher):
    n = p * q
    phi = (p-1)*(q-1)
    d = pow(e, -1, phi)
    message = ''.join([chr((c ** d) % n) for c in cipher])
    return message

p = int(input("Enter prime p: "))
q = int(input("Enter prime q: "))
e = int(input("Enter public key e: "))
cipher = list(map(int, input("Enter cipher numbers separated by space: ").split()))
plain_text = rsa_decrypt(p, q, e, cipher)
print("Decrypted Text:", plain_text)
