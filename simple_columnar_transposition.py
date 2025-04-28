def columnar_encrypt(message, key):
    n = len(key)
    rows = (len(message) + n - 1) // n
    message += '_' * (rows * n - len(message))
    matrix = ['' for _ in range(n)]
    for i in range(len(message)):
        matrix[i % n] += message[i]
    order = sorted(range(len(key)), key=lambda x: key[x])
    cipher = ''
    for index in order:
        cipher += matrix[index]
    return cipher

message = input("Enter message: ")
key = input("Enter key (no spaces, like '4312'): ")
cipher_text = columnar_encrypt(message, key)
print("Encrypted Text:", cipher_text)
