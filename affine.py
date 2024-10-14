def affine_encrypt(plaintext, a, b):
    encrypted = ""
    for char in plaintext:
        if char.isalpha():  # Check if character is a letter
            x = ord(char.lower()) - ord('a')  # Convert char to 0-25
            encrypted_char = (a * x + b) % 26  # Apply affine transformation
            encrypted += chr(encrypted_char + ord('a'))  # Convert back to char
        else:
            encrypted += char  # Non-alpha characters remain unchanged
    return encrypted

def affine_decrypt(ciphertext, a, b):
    # Finding the modular multiplicative inverse of 'a' under modulo 26
    a_inv = pow(a, -1, 26)
    decrypted = ""
    for char in ciphertext:
        if char.isalpha():  # Check if character is a letter
            y = ord(char.lower()) - ord('a')  # Convert char to 0-25
            decrypted_char = (a_inv * (y - b)) % 26  # Apply inverse transformation
            decrypted += chr(decrypted_char + ord('a'))  # Convert back to char
        else:
            decrypted += char  # Non-alpha characters remain unchanged
    return decrypted

# Constants
a = 15
b = 20

# Message
plaintext = "I am learning information security"
# Remove spaces for encryption
plaintext_no_spaces = plaintext.replace(" ", "").lower()

# Encrypt the message
encrypted_message = affine_encrypt(plaintext_no_spaces, a, b)
print("Encrypted message:", encrypted_message)

# Decrypt the message
decrypted_message = affine_decrypt(encrypted_message, a, b)
print("Decrypted message:", decrypted_message)
