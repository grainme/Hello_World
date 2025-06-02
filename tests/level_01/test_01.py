import sys
import os
import pytest

# Add the parent directory to the Python path to import main.py
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../..'))

from main import hello_world


class TestLevel01:
    """Test suite for Level 01: Hello World functionality."""
    
    def test_hello_world_returns_correct_string(self):
        """Test that hello_world() returns exactly 'Hello, World!'"""
        result = hello_world()
        expected = "Hello, World!"
        assert result == expected, f"Expected '{expected}', but got '{result}'"
    
    def test_hello_world_returns_string_type(self):
        """Test that hello_world() returns a string type."""
        result = hello_world()
        assert isinstance(result, str), f"Expected string type, but got {type(result)}"
    
    def test_hello_world_exact_capitalization(self):
        """Test that capitalization is exactly correct."""
        result = hello_world()
        assert "Hello, World!" == result, "Capitalization must be exact: 'Hello, World!'"
    
    def test_hello_world_punctuation(self):
        """Test that punctuation is correct (comma and exclamation mark)."""
        result = hello_world()
        assert "," in result, "Missing comma in greeting"
        assert "!" in result, "Missing exclamation mark"
        assert result.endswith("!"), "String should end with exclamation mark"


if __name__ == "__main__":
    # Run the tests
    pytest.main([__file__, "-v"]) 