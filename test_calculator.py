import pytest
from calculator import add, subtract, multiply, divide


def test_add():
    """Test addition."""
    assert add(2, 3) == 5


def test_subtract():
    """Test subtraction."""
    assert subtract(10, 4) == 6


def test_multiply():
    """Test multiplication."""
    assert multiply(3, 5) == 15


def test_divide():
    """Test division."""
    assert divide(10, 2) == 5


def test_division_by_zero():
    """Test division by zero exception."""
    with pytest.raises(ValueError):
        divide(10, 0)
