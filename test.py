# Write unit tests here
import pytest
from main import function_to_test

# Sample
def testing_def():
    assert(function_to_test(1, 0) == -1)

def testing_above_two():
    assert(function_to_test(3, 0) == 0)

def testing_equal_two():
    assert(function_to_test(2, 0) == 1)

def testing_two_equal_one():
    assert(function_to_test(1, 1) == 2)

# Test with
# pytest -q test.py