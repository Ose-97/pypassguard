import random
import string
from typing import Optional

def generate_password(length: int = 12, include_special: bool = True) -> str:
    """
    Generate a random password with specified length and character sets.
    
    Args:
        length (int): Length of the password (default: 12)
        include_special (bool): Whether to include special characters (default: True)
        
    Returns:
        str: Generated password
        
    Raises:
        ValueError: If length is less than 4
        
    Example:
        >>> generate_password(12)
        'aB3#xY7!pQ9@'
        >>> generate_password(8, include_special=False)
        'aB3xY7pQ'
    """
    if length < 4:
        raise ValueError("Password length must be at least 4 characters")
    
    # Define character sets
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    special = '!@#$%^&*()_+-=[]{};:,.<>?'
    
    # Build the character pool based on requirements
    char_pool = lowercase + uppercase + digits
    if include_special:
        char_pool += special
    
    # Ensure password contains at least one of each required character type
    password_chars = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(digits),
    ]
    
    if include_special:
        password_chars.append(random.choice(special))
    
    # Fill the rest of the password with random characters from the pool
    remaining_length = length - len(password_chars)
    password_chars.extend(random.choice(char_pool) for _ in range(remaining_length))
    
    # Shuffle the characters to randomize the order
    random.shuffle(password_chars)
    
    return ''.join(password_chars)

def generate_multiple_passwords(count: int = 5, length: int = 12, include_special: bool = True) -> list:
    """
    Generate multiple random passwords.
    
    Args:
        count (int): Number of passwords to generate (default: 5)
        length (int): Length of each password (default: 12)
        include_special (bool): Whether to include special characters (default: True)
        
    Returns:
        list: List of generated passwords
    """
    return [generate_password(length, include_special) for _ in range(count)]

if __name__ == "__main__":
    # Test the generator
    print("Testing Password Generator:")
    print("=" * 30)
    
    # Test basic generation
    print("1. Basic password (12 chars):")
    print(f"   {generate_password()}")
    
    # Test without special characters
    print("\n2. Password without special chars:")
    print(f"   {generate_password(include_special=False)}")
    
    # Test custom length
    print("\n3. Short password (8 chars):")
    print(f"   {generate_password(8)}")
    
    # Test multiple passwords
    print("\n4. Multiple passwords:")
    for i, pwd in enumerate(generate_multiple_passwords(3, 10), 1):
        print(f"   {i}. {pwd}")
    
    # Test error handling
    print("\n5. Testing error handling:")
    try:
        generate_password(3)
    except ValueError as e:
        print(f"   Error (expected): {e}")