def custom_hash(input_string):
    # Initialize hash value
    hash_value = 5381
    
    for char in input_string:
        # Get ASCII value of the character
        ascii_value = ord(char)
        
        # Update hash value using the given formula
        hash_value = ((hash_value << 5) + hash_value) + ascii_value  # Equivalent to hash_value * 33 + ascii_value
        
        # Ensure the hash value stays within 32 bits
        hash_value &= 0xFFFFFFFF  # Apply a 32-bit mask

    return hash_value

# Example usage
input_string = "Cryptographic Protocols"
hash_result = custom_hash(input_string)
print("Hash value:", hash_result)
