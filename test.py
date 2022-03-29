# Write unit tests here
import pytest
from main import function_to_test


def test_one():
    assert function_to_test(2, 0) == 1
def test_two():
    assert function_to_test(3, 69) == 0
def test_three():
    assert function_to_test(1, 1) == 2
def test_four():
    assert function_to_test(-1, 420) == -1

# Test with
# pytest -q test.py