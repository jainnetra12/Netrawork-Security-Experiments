def caesar_encrypt(text, shift):
    encrypted = ""
    for char in text:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            encrypted += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            encrypted += char
    return encrypted

text = input("Enter text to encrypt: ")
shift = int(input("Enter shift value: "))
cipher_text = caesar_encrypt(text, shift)
print("Encrypted Text:", cipher_text)
