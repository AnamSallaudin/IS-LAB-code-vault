import numpy as np

def prepare_plaintext(plaintext):
    # Remove spaces and convert to uppercase
    cleaned = plaintext.replace(" ", "").upper()
    return cleaned

def text_to_numbers(text):
    # Convert text to numerical values (A=0, B=1, ..., Z=25)
    return [ord(char) - ord('A') for char in text]

def numbers_to_text(numbers):
    # Convert numerical values back to text
    return ''.join(chr(num + ord('A')) for num in numbers)

def hill_encrypt(plaintext, key_matrix):
    # Prepare the plaintext
    prepared_text = prepare_plaintext(plaintext)
    
    # Pad the plaintext if necessary to make it even
    if len(prepared_text) % 2 != 0:
        prepared_text += 'X'  # Padding with 'X'

    # Convert plaintext to numbers
    plaintext_numbers = text_to_numbers(prepared_text)

    # Reshape into pairs
    pairs = np.array(plaintext_numbers).reshape(-1, 2)

    # Encrypt using the Hill cipher
    encrypted_numbers = (pairs @ key_matrix) % 26

    # Convert back to text
    encrypted_text = numbers_to_text(encrypted_numbers.flatten())

    return encrypted_text

# Key matrix
key_matrix = np.array([[3, 3], [2, 7]])

# Message
plaintext = "We live in an insecure world"

# Encrypt the message
encrypted_message = hill_encrypt(plaintext, key_matrix)
print("Encrypted message:", encrypted_message)
