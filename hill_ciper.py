import numpy as np

def hill_encrypt(message, key_matrix):
    message = message.replace(" ", "").upper()
    while len(message) % 2 != 0:
        message += 'X'
    cipher = ''
    for i in range(0, len(message), 2):
        block = np.array([[ord(message[i]) - 65], [ord(message[i+1]) - 65]])
        encrypted_block = np.dot(key_matrix, block) % 26
        cipher += chr(encrypted_block[0][0] + 65)
        cipher += chr(encrypted_block[1][0] + 65)
    return cipher

message = input("Enter message: ")
key_elements = list(map(int, input("Enter 4 elements of key matrix (row-wise): ").split()))
key_matrix = np.array(key_elements).reshape(2, 2)
cipher_text = hill_encrypt(message, key_matrix)
print("Encrypted Text:", cipher_text)
