def generate_matrix(key):
    matrix = []
    key = key.upper().replace("J", "I")
    for c in key:
        if c not in matrix and c.isalpha():
            matrix.append(c)
    for c in "ABCDEFGHIKLMNOPQRSTUVWXYZ":
        if c not in matrix:
            matrix.append(c)
    return [matrix[i:i+5] for i in range(0, 25, 5)]

def find_position(matrix, char):
    for row in range(5):
        for col in range(5):
            if matrix[row][col] == char:
                return row, col

def playfair_encrypt(text, key):
    matrix = generate_matrix(key)
    text = text.upper().replace("J", "I")
    text = ''.join([c for c in text if c.isalpha()])
    i = 0
    pairs = []
    while i < len(text):
        a = text[i]
        b = text[i + 1] if i + 1 < len(text) else 'X'
        if a == b:
            b = 'X'
        pairs.append((a, b))
        i += 2
    cipher = ''
    for a, b in pairs:
        row1, col1 = find_position(matrix, a)
        row2, col2 = find_position(matrix, b)
        if row1 == row2:
            cipher += matrix[row1][(col1+1)%5] + matrix[row2][(col2+1)%5]
        elif col1 == col2:
            cipher += matrix[(row1+1)%5][col1] + matrix[(row2+1)%5][col2]
        else:
            cipher += matrix[row1][col2] + matrix[row2][col1]
    return cipher

text = input("Enter text to encrypt: ")
key = input("Enter key: ")
cipher_text = playfair_encrypt(text, key)
print("Encrypted Text:", cipher_text)
