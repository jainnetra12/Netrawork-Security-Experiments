def diffie_hellman(p, g, a, b):
    A = pow(g, a, p)
    B = pow(g, b, p)
    key_a = pow(B, a, p)
    key_b = pow(A, b, p)
    return key_a, key_b

p = int(input("Enter prime number p: "))
g = int(input("Enter primitive root g: "))
a = int(input("Enter private key of User A: "))
b = int(input("Enter private key of User B: "))
key_a, key_b = diffie_hellman(p, g, a, b)
print("Shared Key at A:", key_a)
print("Shared Key at B:", key_b)
