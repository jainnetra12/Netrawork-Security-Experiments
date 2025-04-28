def vigenere_encrypt(text, key):
    encrypted = ""
    key = key.lower()
    key_index = 0
    for char in text:
        if char.isalpha():
            shift = ord(key[key_index % len(key)]) - ord('a')
            shift_base = ord('A') if char.isupper() else ord('a')
            encrypted += chr((ord(char) - shift_base + shift) % 26 + shift_base)
            key_index += 1
        else:
            encrypted += char
    return encrypted

text = input("Enter text to encrypt: ")
key = input("Enter key: ")
cipher_text = vigenere_encrypt(text, key)
print("Encrypted Text:", cipher_text)
