def create_playfair_matrix(key):
    # Create a 5x5 matrix for Playfair cipher
    matrix = []
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"  # Note: I/J are combined
    key = key.upper().replace("J", "I")  # Replace J with I

    # Add unique letters from the key to the matrix
    for char in key:
        if char not in matrix and char in alphabet:
            matrix.append(char)

    # Fill the matrix with remaining letters of the alphabet
    for char in alphabet:
        if char not in matrix:
            matrix.append(char)

    # Convert the matrix into a 5x5 list of lists
    return [matrix[i:i + 5] for i in range(0, 25, 5)]

def prepare_plaintext(plaintext):
    # Remove spaces and make uppercase
    plaintext = plaintext.replace(" ", "").upper().replace("J", "I")
    
    # Handle repeated letters by inserting an X
    prepared = []
    i = 0
    while i < len(plaintext):
        if i + 1 < len(plaintext) and plaintext[i] == plaintext[i + 1]:
            prepared.append(plaintext[i])
            prepared.append('X')  # Insert X for repetition
            i += 1
        else:
            prepared.append(plaintext[i])
            if i + 1 < len(plaintext):
                prepared.append(plaintext[i + 1])
                i += 2
            else:
                prepared.append('X')  # Append X if odd number of chars
                i += 1

    return ''.join(prepared)

def playfair_encrypt(plaintext, key):
    matrix = create_playfair_matrix(key)
    prepared_text = prepare_plaintext(plaintext)
    encrypted = ""

    # Function to find the position of a character in the matrix
    def find_position(char):
        for i in range(5):
            for j in range(5):
                if matrix[i][j] == char:
                    return i, j
        return None

    # Encrypt the prepared text in pairs
    for i in range(0, len(prepared_text), 2):
        char1 = prepared_text[i]
        char2 = prepared_text[i + 1]

        row1, col1 = find_position(char1)
        row2, col2 = find_position(char2)

        if row1 == row2:  # Same row
            encrypted += matrix[row1][(col1 + 1) % 5]
            encrypted += matrix[row2][(col2 + 1) % 5]
        elif col1 == col2:  # Same column
            encrypted += matrix[(row1 + 1) % 5][col1]
            encrypted += matrix[(row2 + 1) % 5][col2]
        else:  # Rectangle
            encrypted += matrix[row1][col2]
            encrypted += matrix[row2][col1]

    return encrypted

# Message and key
plaintext = "The key is hidden under the door pad"
key = "GUIDANCE"

# Encrypt the message
encrypted_message = playfair_encrypt(plaintext, key)
print("Encrypted message:", encrypted_message)
