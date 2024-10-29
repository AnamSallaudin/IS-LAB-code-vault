import os
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes
from ecdsa import SigningKey, VerifyingKey, NIST384p

# Generate ECC keys for Commander
def generate_ecc_keys():
    sk = SigningKey.generate(curve=NIST384p)
    vk = sk.get_verifying_key()
    return sk, vk

# Generate RSA keys
def generate_rsa_keys():
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
        backend=default_backend()
    )
    public_key = private_key.public_key()
    return private_key, public_key

# Encrypt Level 2 data using RSA
def encrypt_l2(public_key, data):
    encrypted = public_key.encrypt(
        data.encode(),
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return encrypted

# Decrypt Level 2 data using RSA
def decrypt_l2(private_key, encrypted_data):
    decrypted = private_key.decrypt(
        encrypted_data,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return decrypted.decode()

# Sign Level 1 data using ECC
def sign_l1(private_key, data):
    signature = private_key.sign(data.encode())
    return signature

# Verify Level 1 data using ECC
def verify_l1(public_key, signature, data):
    try:
        public_key.verify(signature, data.encode())
        return True
    except Exception:
        return False

# Read message from file
def read_message_from_file(filename):
    with open(filename, 'r') as file:
        return file.read()

# Main function to demonstrate the usage
def main():
    # Generate keys
    ecc_sk, ecc_vk = generate_ecc_keys()
    rsa_sk, rsa_vk = generate_rsa_keys()

    # Read L1 data from file
    filename = 'message1.txt'
    
    if not os.path.exists(filename):
        print(f"File '{filename}' not found.")
        return
    
    level_1_data = read_message_from_file(filename)
    level_2_data = "This is Level 2 public data."

    # Sign L1 data
    l1_signature = sign_l1(ecc_sk, level_1_data)
    
    # Encrypt L2 data
    l2_encrypted = encrypt_l2(rsa_vk, level_2_data)

    # User role input
    role = input("Enter your role (commander or personnel): ").strip().lower()

    # Use case based on user role
    if role == "commander":
        print("\nAs a commander, you can access both L1 and L2 data.")
        
        # Ask if the commander wants to read the L1 data
        read_l1 = input("Do you want to read Level 1 data? (yes/no): ").strip().lower()
        if read_l1 == "yes":
            print("\nLevel 1 data (from file):")
            print(level_1_data)
            # Verify L1 data
            l1_decrypt_status = verify_l1(ecc_vk, l1_signature, level_1_data)
            print("Level 1 data verification successful:", l1_decrypt_status)

        # Decrypt L2 data
        l2_decrypted = decrypt_l2(rsa_sk, l2_encrypted)
        print("\nDecrypted Level 2 data:", l2_decrypted)

    elif role == "personnel":
        print("\nAs personnel, you can access only L2 data.")

        # Attempt to decrypt L2 data
        l2_decrypted = decrypt_l2(rsa_sk, l2_encrypted)
        print("\nDecrypted Level 2 data:", l2_decrypted)

        # Attempt to access L1 data
        print("Access to Level 1 data is restricted for personnel.")

    else:
        print("Invalid role. Please enter 'commander' or 'personnel'.")

if __name__ == "__main__":
    main()
