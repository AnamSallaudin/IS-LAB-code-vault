def vigenere_encrypt(plaintext, key):
    encrypted = ""
    key_length = len(key)
    key_as_int = [ord(i) - ord('a') for i in key]  # Convert key to numerical values
    plaintext_int = [ord(i) - ord('a') for i in plaintext]  # Convert plaintext to numerical values

    for i in range(len(plaintext_int)):
        value = (plaintext_int[i] + key_as_int[i % key_length]) % 26
        encrypted += chr(value + ord('a'))  # Convert back to char

    return encrypted

def vigenere_decrypt(ciphertext, key):
    decrypted = ""
    key_length = len(key)
    key_as_int = [ord(i) - ord('a') for i in key]  # Convert key to numerical values
    ciphertext_int = [ord(i) - ord('a') for i in ciphertext]  # Convert ciphertext to numerical values

    for i in range(len(ciphertext_int)):
        value = (ciphertext_int[i] - key_as_int[i % key_length]) % 26
        decrypted += chr(value + ord('a'))  # Convert back to char

    return decrypted

# Message
plaintext = "the house is being sold tonight"
# Remove spaces and convert to lowercase for encryption
plaintext_no_spaces = plaintext.replace(" ", "").lower()
key = "dollars"

# Encrypt the message
encrypted_message = vigenere_encrypt(plaintext_no_spaces, key)
print("Encrypted message:", encrypted_message)

# Decrypt the message
decrypted_message = vigenere_decrypt(encrypted_message, key)
print("Decrypted message:", decrypted_message)
