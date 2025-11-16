import unittest
import sys
import os

# Add src to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from validator import validate_password, get_validation_feedback, validate_password_with_feedback

class TestValidator(unittest.TestCase):
    
    def test_valid_password(self):
        """Test that a strong password passes validation"""
        password = "StrongP@ss123!"
        is_valid, results = validate_password(password)
        self.assertTrue(is_valid)
        self.assertTrue(all(results.values()))
    
    def test_short_password(self):
        """Test that short password fails length check"""
        password = "Short1!"
        is_valid, results = validate_password(password)
        self.assertFalse(is_valid)
        self.assertFalse(results['length'])
    
    def test_no_uppercase(self):
        """Test password without uppercase"""
        password = "lowercase123!"
        is_valid, results = validate_password(password)
        self.assertFalse(is_valid)
        self.assertFalse(results['uppercase'])
    
    def test_no_lowercase(self):
        """Test password without lowercase"""
        password = "UPPERCASE123!"
        is_valid, results = validate_password(password)
        self.assertFalse(is_valid)
        self.assertFalse(results['lowercase'])
    
    def test_no_digits(self):
        """Test password without digits"""
        password = "NoDigitsHere!"
        is_valid, results = validate_password(password)
        self.assertFalse(is_valid)
        self.assertFalse(results['digits'])
    
    def test_no_special_chars(self):
        """Test password without special characters"""
        password = "NoSpecial123"
        is_valid, results = validate_password(password)
        self.assertFalse(is_valid)
        self.assertFalse(results['special'])
    
    def test_common_weak_patterns(self):
        """Test detection of common weak patterns"""
        weak_passwords = ["password123", "qwertyuiop", "123456789"]
        
        for password in weak_passwords:
            is_valid, results = validate_password(password)
            self.assertFalse(is_valid)
            self.assertFalse(results['common_patterns'])
    
    def test_sequential_chars(self):
        """Test detection of sequential characters"""
        sequential_passwords = ["abc123!", "123abc@", "xyz789#"]
        
        for password in sequential_passwords:
            is_valid, results = validate_password(password)
            self.assertFalse(is_valid)
            self.assertFalse(results['sequential'])
    
    def test_feedback_messages(self):
        """Test feedback message generation"""
        password = "weak"  # Fails multiple checks
        is_valid, results = validate_password(password)
        feedback = get_validation_feedback(results)
        
        self.assertFalse(is_valid)
        self.assertGreater(len(feedback), 0)
        self.assertIn("at least 8 characters long", feedback[0])
    
    def test_validate_with_feedback(self):
        """Test the combined validation and feedback function"""
        password = "StrongP@ss123!"
        is_valid, feedback = validate_password_with_feedback(password)
        
        self.assertTrue(is_valid)
        self.assertEqual(len(feedback), 0)

if __name__ == '__main__':
    unittest.main()