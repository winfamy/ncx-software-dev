# Write unit tests here
import pytest
from main import function_to_test

# Sample
def test1():
    assert(function_to_test(1,1) == 2)
def test2():
    assert(function_to_test(2,100) == 1)
def test3():
    assert(function_to_test(4,0) == 0)
def test4():
    assert(function_to_test(-1,420) == -1)

# Test with
# pytest -q test.py