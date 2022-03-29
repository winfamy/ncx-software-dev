# Write unit tests here
import pytest
from main import function_to_test

# Sample
# def test_example():
#     assert(1 == 1)
#     assert(1 == 2)

# Test with
# pytest -q test.py

def test_return1():
    assert(function_to_test(2, 0) == 1)

def test_return0():
    assert(function_to_test(3, 0) == 0)

def test_return2():
    assert(function_to_test(1, 1) == 2)

def test_default(capsys):
    assert(function_to_test(-1, -1) == -1)
    output = capsys.readouterr()
    assert(output.out == "ur dumb !!!\n")