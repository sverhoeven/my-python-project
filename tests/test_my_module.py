#!/usr/bin/env python

"""Tests for the my_python_package.my_module module.
"""
import pytest
from my_python_package import my_module


def test_hello():
    assert my_module.hello('nlesc') == 'Hello nlesc!'


def test_something():
    assert True


def test_with_error():
    with pytest.raises(ValueError):
        # Do something that raises a ValueError
        raise(ValueError)


# Fixture example
@pytest.fixture
def an_object():
    return {}


def test_my_module(an_object):
    assert an_object == {}
