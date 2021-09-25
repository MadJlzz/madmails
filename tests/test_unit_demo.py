"""This module shows how to write some unit tests."""

import os


# Typically, this function is the one you will find in your application.
def add(a: int, b: int) -> int:
    return a + b


def remove_file(filepath: str) -> None:
    os.remove(filepath)


# This is a test case.
# You have to prefix your test function with test_* for pytest to find them.
def test_add_positive_ok():
    assert add(1, 1) == 2


# Another example of test.
def test_add_negative_ok():
    assert add(-1, 1) == 0


# Here we have a test that depends on other function.
# The classic problem is that we don't care of the actual execution of the method
# but more on it's return state. You can fake the return of a function by mocking it.
def test_remove_file(mocker):
    # We replace dynamically the implementation of os.remove with a fake one.
    mocker.patch('os.remove')

    # We call our method that we want to test.
    remove_file('file')

    # Example of check to see if our mock was called with the correct parameter.
    os.remove.assert_called_once_with('file')
