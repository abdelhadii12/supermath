import pytest
from supermath1.arithmetique import addition, soustraction, multiplication, division

def test_addition():
    assert addition(1, 2) == 3
    assert addition(-1, 1) == 0
    assert addition(-1, -1) == -2

def test_soustraction():
    assert soustraction(2, 1) == 1
    assert soustraction(-1, -1) == 0
    assert soustraction(-1, 1) == -2

def test_multiplication():
    assert multiplication(2, 3) == 6
    assert multiplication(-1, 1) == -1
    assert multiplication(0, 5) == 0

def test_division():
    assert division(6, 2) == 3
    assert division(5, 0) is None  # Test pour division par zéro
    assert division(-6, -2) == 3


