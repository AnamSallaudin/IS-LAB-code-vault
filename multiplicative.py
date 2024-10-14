def multiplicative_encrypt(plaintext, k):
    encrypted = ""
    for char in plaintext:
        if char.isalpha():  # Check if character is a letter
            x = ord(char.lower()) - ord('a')  # Convert char to 0-25
            encrypted_char = (k * x) % 26  # Apply multiplicative transformation
            encrypted += chr(encrypted_char + ord('a'))  # Convert back to char
        else:
            encrypted += char  # Non-alpha characters remain unchanged
    return encrypted

def multiplicative_decrypt(ciphertext, k):
    # Finding the modular multiplicative inverse of 'k' under modulo 26
    k_inv = pow(k, -1, 26)
    decrypted = ""
    for char in ciphertext:
        if char.isalpha():  # Check if character is a letter
            y = ord(char.lower()) - ord('a')  # Convert char to 0-25
            decrypted_char = (k_inv * y) % 26  # Apply inverse transformation
            decrypted += chr(decrypted_char + ord('a'))  # Convert back to char
        else:
            decrypted += char  # Non-alpha characters remain unchanged
    return decrypted

# Constants
k = 15

# Message
plaintext = "I am learning information security"
# Remove spaces for encryption
plaintext_no_spaces = plaintext.replace(" ", "").lower()

# Encrypt the message
encrypted_message = multiplicative_encrypt(plaintext_no_spaces, k)
print("Encrypted message:", encrypted_message)

# Decrypt the message
decrypted_message = multiplicative_decrypt(encrypted_message, k)
print("Decrypted message:", decrypted_message)
