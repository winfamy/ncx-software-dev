# Write unit tests here
import pytest
from main import function_to_test

# Sample
def test_example():
    assert(function_to_test(1, 0) == -1)
    assert(function_to_test(2, 0) == 1)
    assert(function_to_test(3, 0) == 0)
    assert(function_to_test(1, 1) == 2)

# Test with
# pytest -q test.py