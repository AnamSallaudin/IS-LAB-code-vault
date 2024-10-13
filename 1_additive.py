def encrypt(message, key):
    # Remove spaces and convert to uppercase
    message = message.replace(" ", "").upper()
    encrypted_message = ""

    for char in message:
        if 'A' <= char <= 'Z':
            # Encrypt the character
            new_char = chr((ord(char) - ord('A') + key) % 26 + ord('A'))
            encrypted_message += new_char
        else:
            encrypted_message += char  # Non-alphabetic characters remain unchanged

    return encrypted_message

def decrypt(encrypted_message, key):
    decrypted_message = ""

    for char in encrypted_message:
        if 'A' <= char <= 'Z':
            # Decrypt the character
            new_char = chr((ord(char) - ord('A') - key) % 26 + ord('A'))
            decrypted_message += new_char
        else:
            decrypted_message += char  # Non-alphabetic characters remain unchanged

    return decrypted_message

# Example usage
message = "I am learning information security"
key = 20

encrypted = encrypt(message, key)
decrypted = decrypt(encrypted, key)

print("Encrypted message:", encrypted)
print("Decrypted message:", decrypted)
