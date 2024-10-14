def autokey_encrypt(plaintext, key):
    encrypted = ""
    key_length = len(plaintext)
    key_extended = [key]  # Start with the initial key value

    # Convert plaintext to numerical values (0-25)
    plaintext_int = [ord(char) - ord('a') for char in plaintext if char.isalpha()]

    for i in range(len(plaintext_int)):
        if i > 0:
            key_extended.append(plaintext_int[i - 1])  # Use the previous plaintext letter as part of the key

        # Encrypt the character
        value = (plaintext_int[i] + key_extended[i]) % 26
        encrypted += chr(value + ord('a'))  # Convert back to character

    return encrypted

def autokey_decrypt(ciphertext, key):
    decrypted = ""
    key_extended = [key]  # Start with the initial key value

    # Convert ciphertext to numerical values (0-25)
    ciphertext_int = [ord(char) - ord('a') for char in ciphertext]

    for i in range(len(ciphertext_int)):
        # Decrypt the character
        value = (ciphertext_int[i] - key_extended[i]) % 26
        decrypted += chr(value + ord('a'))  # Convert back to character

        if i < len(ciphertext_int) - 1:
            key_extended.append(value)  # Add the decrypted letter to the key for the next round

    return decrypted

# Message
plaintext = "the house is being sold tonight"
# Remove spaces and convert to lowercase for encryption
plaintext_no_spaces = plaintext.replace(" ", "").lower()
key = 7

# Encrypt the message
encrypted_message = autokey_encrypt(plaintext_no_spaces, key)
print("Encrypted message:", encrypted_message)

# Decrypt the message
decrypted_message = autokey_decrypt(encrypted_message, key)
print("Decrypted message:", decrypted_message)
