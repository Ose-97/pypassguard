import unittest
import sys
import os
import re

# Add src to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from generator import generate_password, generate_multiple_passwords

class TestGenerator(unittest.TestCase):
    
    def test_generate_password_length(self):
        """Test that generated password has correct length"""
        for length in [8, 12, 16]:
            password = generate_password(length)
            self.assertEqual(len(password), length)
    
    def test_generate_password_characters(self):
        """Test that password contains required character types"""
        password = generate_password(12)
        
        # Check for at least one lowercase
        self.assertTrue(any(c.islower() for c in password))
        # Check for at least one uppercase
        self.assertTrue(any(c.isupper() for c in password))
        # Check for at least one digit
        self.assertTrue(any(c.isdigit() for c in password))
        # Check for at least one special character
        self.assertTrue(any(c in '!@#$%^&*()_+-=[]{};:,.<>?' for c in password))
    
    def test_generate_password_no_special(self):
        """Test password generation without special characters"""
        password = generate_password(12, include_special=False)
        
        # Should not contain special characters
        self.assertFalse(any(c in '!@#$%^&*()_+-=[]{};:,.<>?' for c in password))
        # But should still have other types
        self.assertTrue(any(c.islower() for c in password))
        self.assertTrue(any(c.isupper() for c in password))
        self.assertTrue(any(c.isdigit() for c in password))
    
    def test_generate_multiple_passwords(self):
        """Test generating multiple passwords"""
        passwords = generate_multiple_passwords(5, 10)
        
        self.assertEqual(len(passwords), 5)
        for password in passwords:
            self.assertEqual(len(password), 10)
            self.assertTrue(any(c.islower() for c in password))
            self.assertTrue(any(c.isupper() for c in password))
            self.assertTrue(any(c.isdigit() for c in password))
    
    def test_password_uniqueness(self):
        """Test that generated passwords are unique"""
        passwords = generate_multiple_passwords(10, 12)
        unique_passwords = set(passwords)
        self.assertEqual(len(passwords), len(unique_passwords))
    
    def test_invalid_length(self):
        """Test error handling for invalid length"""
        with self.assertRaises(ValueError):
            generate_password(3)

if __name__ == '__main__':
    unittest.main()