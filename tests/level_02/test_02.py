import sys
import os
import pytest

# Add the parent directory to the Python path to import main.py
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../..'))

from main import hello_ninefive


class TestLevel02:
    """Test suite for Level 02: Hello ninefive functionality."""
    
    def test_hello_ninefive_returns_correct_string(self):
        """Test that hello_ninefive() returns exactly 'Hello, ninefive!'"""
        result = hello_ninefive()
        expected = "Hello, ninefive!"
        assert result == expected, f"Expected '{expected}', but got '{result}'"
    
    def test_hello_ninefive_returns_string_type(self):
        """Test that hello_ninefive() returns a string type."""
        result = hello_ninefive()
        assert isinstance(result, str), f"Expected string type, but got {type(result)}"
    
    def test_hello_ninefive_lowercase_n(self):
        """Test that 'ninefive' uses lowercase 'n' (not 'Ninefive')."""
        result = hello_ninefive()
        assert "ninefive" in result, "Should contain 'ninefive' with lowercase 'n'"
        assert "Ninefive" not in result, "Should NOT contain 'Ninefive' with uppercase 'N'"
    
    def test_hello_ninefive_punctuation(self):
        """Test that punctuation is correct (comma and exclamation mark)."""
        result = hello_ninefive()
        assert "," in result, "Missing comma in greeting"
        assert "!" in result, "Missing exclamation mark"
        assert result.endswith("!"), "String should end with exclamation mark"
    
    def test_hello_ninefive_exact_format(self):
        """Test the exact format and spacing."""
        result = hello_ninefive()
        expected = "Hello, ninefive!"
        assert result == expected, f"Expected exact format: '{expected}', got: '{result}'"


if __name__ == "__main__":
    # Run the tests
    pytest.main([__file__, "-v"]) 