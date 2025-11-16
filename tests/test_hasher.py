import unittest
import sys
import os

# Add src to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from hasher import hash_password

class TestHasher(unittest.TestCase):
    
    def test_hash_password(self):
        """Test that hash_password returns a valid SHA-256 hash"""
        # Test with a simple password
        password = "test123"
        hashed = hash_password(password)
        
        # Check that it returns a string
        self.assertIsInstance(hashed, str)
        
        # Check that the hash is 64 characters long (SHA-256 hex digest)
        self.assertEqual(len(hashed), 64)
        
        # Check that it only contains hexadecimal characters
        self.assertTrue(all(c in '0123456789abcdef' for c in hashed))
        
        # Test that same password gives same hash
        same_hash = hash_password(password)
        self.assertEqual(hashed, same_hash)
        
        # Test that different passwords give different hashes
        different_password = "test124"
        different_hash = hash_password(different_password)
        self.assertNotEqual(hashed, different_hash)

if __name__ == '__main__':
    unittest.main()