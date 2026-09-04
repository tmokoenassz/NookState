# test_nookstate.py
"""
Tests for NookState module.
"""

import unittest
from nookstate import NookState

class TestNookState(unittest.TestCase):
    """Test cases for NookState class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = NookState()
        self.assertIsInstance(instance, NookState)
        
    def test_run_method(self):
        """Test the run method."""
        instance = NookState()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
