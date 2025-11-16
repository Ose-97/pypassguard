import hashlib

def hash_password(password: str) -> str:
    """
    Hash a password using SHA-256 algorithm.
    
    Args:
        password (str): The password to hash
        
    Returns:
        str: SHA-256 hash as a hexadecimal string
    """
    password_bytes = password.encode('utf-8')
    hash_object = hashlib.sha256(password_bytes)
    return hash_object.hexdigest()

if __name__ == "__main__":
    # Test the function
    test_password = "password123"
    hashed = hash_password(test_password)
    print(f"Password: {test_password}")
    print(f"SHA-256 Hash: {hashed}")
    print(f"Hash length: {len(hashed)} characters")