import re
from typing import Dict, List, Tuple
import sys
import os

# Add the project root to Python path to import utils
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
from utils.config import PASSWORD_REQUIREMENTS

def validate_password(password: str) -> Tuple[bool, Dict]:
    """
    Validate a password against security criteria.
    
    Args:
        password (str): Password to validate
        
    Returns:
        Tuple[bool, Dict]: (is_valid, validation_details)
        
    Example:
        >>> validate_password("Weak1!")
        (False, {'length': False, 'uppercase': True, ...})
    """
    requirements = PASSWORD_REQUIREMENTS
    results = {}
    
    # Check length
    results['length'] = len(password) >= requirements['min_length']
    
    # Check character types
    results['uppercase'] = (
        not requirements['require_uppercase'] or 
        any(c.isupper() for c in password)
    )
    
    results['lowercase'] = (
        not requirements['require_lowercase'] or 
        any(c.islower() for c in password)
    )
    
    results['digits'] = (
        not requirements['require_digits'] or 
        any(c.isdigit() for c in password)
    )
    
    results['special'] = (
        not requirements['require_special_chars'] or 
        any(c in requirements['special_chars'] for c in password)
    )
    
    # Check for common weak patterns
    results['common_patterns'] = not _has_common_weak_patterns(password)
    
    # Check for sequential characters
    results['sequential'] = not _has_sequential_chars(password)
    
    # Calculate overall validity
    is_valid = all(results.values())
    
    return is_valid, results

def get_validation_feedback(validation_results: Dict) -> List[str]:
    """
    Generate user-friendly feedback based on validation results.
    
    Args:
        validation_results (Dict): Results from validate_password
        
    Returns:
        List[str]: List of feedback messages
    """
    feedback = []
    requirements = PASSWORD_REQUIREMENTS
    
    if not validation_results['length']:
        feedback.append(f"Password must be at least {requirements['min_length']} characters long")
    
    if not validation_results['uppercase']:
        feedback.append("Password must contain at least one uppercase letter")
    
    if not validation_results['lowercase']:
        feedback.append("Password must contain at least one lowercase letter")
    
    if not validation_results['digits']:
        feedback.append("Password must contain at least one digit")
    
    if not validation_results['special']:
        special_chars = requirements['special_chars']
        feedback.append(f"Password must contain at least one special character ({special_chars})")
    
    if not validation_results['common_patterns']:
        feedback.append("Password contains common weak patterns (like 'password', '123', etc.)")
    
    if not validation_results['sequential']:
        feedback.append("Password contains sequential characters (like 'abc', '123', etc.)")
    
    return feedback

def _has_common_weak_patterns(password: str) -> bool:
    """Check for common weak password patterns."""
    common_weak = [
        'password', '123456', 'qwerty', 'admin', 'welcome',
        'letmein', 'monkey', 'dragon', 'baseball', 'football',
        'iloveyou', 'master', 'superman', 'password1', 'hello'
    ]
    
    password_lower = password.lower()
    return any(pattern in password_lower for pattern in common_weak)

def _has_sequential_chars(password: str) -> bool:
    """Check for sequential characters (abc, 123, etc.)."""
    if len(password) < 3:
        return False
    
    for i in range(len(password) - 2):
        # Check alphabetical sequences
        if (ord(password[i].lower()) + 1 == ord(password[i+1].lower()) and
            ord(password[i].lower()) + 2 == ord(password[i+2].lower())):
            return True
        
        # Check numerical sequences
        if (password[i].isdigit() and password[i+1].isdigit() and password[i+2].isdigit() and
            int(password[i]) + 1 == int(password[i+1]) and
            int(password[i]) + 2 == int(password[i+2])):
            return True
    
    return False

def validate_password_with_feedback(password: str) -> Tuple[bool, List[str]]:
    """
    Validate password and return feedback in one function.
    
    Args:
        password (str): Password to validate
        
    Returns:
        Tuple[bool, List[str]]: (is_valid, feedback_messages)
    """
    is_valid, results = validate_password(password)
    feedback = get_validation_feedback(results)
    return is_valid, feedback

if __name__ == "__main__":
    # Test the validator
    test_passwords = [
        "StrongP@ss123!",
        "weak",
        "Password123",
        "abc123!@#",
        "123456789",
        "qwertyuiop",
        "Admin123!",
        "aB1!aB1!aB1!",
        "sequential123",
        "password1!"
    ]
    
    print("Password Validator Test:")
    print("=" * 50)
    
    for password in test_passwords:
        is_valid, results = validate_password(password)
        feedback = get_validation_feedback(results)
        
        status = "✅ VALID" if is_valid else "❌ INVALID"
        print(f"\nPassword: {password}")
        print(f"Status: {status}")
        
        if not is_valid:
            print("Issues:")
            for issue in feedback:
                print(f"  - {issue}")
        else:
            print("All requirements met!")
        
        print("-" * 30)