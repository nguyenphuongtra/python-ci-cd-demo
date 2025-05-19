"""Module chứa các test cho app."""

from app import add

def test_add():
    """Test hàm add."""
    assert add(1, 2) == 3
