# Write unit tests here
import pytest
from main import function_to_test

# Sample
def test_example():
    assert(1 == 1)
    #assert(1 == 2)
def test_1():
    assert(function_to_test(2, 1) == 1)
def test_2():
    assert(function_to_test(3, 1) == 0)
def test_3():
    assert(function_to_test(0, 1) == -1)
def test_4():
    assert(function_to_test(1, 1) == 2)

# Test with
# pytest -q test.py