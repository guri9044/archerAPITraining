from cryptography.fernet import Fernet

import os 
os.system('cls' if os.name == 'nt' else 'clear')

print("________________________________________________________________________________________________________________________________________\n\n")
# Generate a key (run once and store it securely, don't hardcode in code)
def generate_key():
    return Fernet.generate_key()

# Encrypt password
def encrypt_password(password: str, key: bytes) -> bytes:
    fernet = Fernet(key)
    encrypted = fernet.encrypt(password.encode())
    return encrypted

# Decrypt password
def decrypt_password(encrypted_password: bytes, key: bytes) -> str:
    fernet = Fernet(key)
    decrypted = fernet.decrypt(encrypted_password).decode()
    return decrypted



    # Generate and save key (do this once and reuse the same key)
key = 'yLcmh4BfdJIEJUqwjd_U13F8pWEgviR_PpHE3edePUQ='.encode()
print(f"Generated Key: {key.decode()}")  # save this securely (env var / secret manager)

# Example usage
password = "api.user"
encrypted = encrypt_password(password, key)
print("Encrypted:", encrypted.decode())

decrypted = decrypt_password(encrypted, key)
print("Decrypted:", decrypted+"\n\n________________________________________________________________________________________________________________________________________")
