def rail_fence_encrypt(text, key):
    rail = ['' for _ in range(key)]
    dir_down = False
    row = 0
    for char in text:
        rail[row] += char
        if row == 0 or row == key - 1:
            dir_down = not dir_down
        row += 1 if dir_down else -1
    return ''.join(rail)

text = input("Enter text to encrypt: ")
key = int(input("Enter number of rails: "))
cipher_text = rail_fence_encrypt(text, key)
print("Encrypted Text:", cipher_text)
