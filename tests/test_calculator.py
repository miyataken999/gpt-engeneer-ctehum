import pytest
from src.calculator import Calculator

def test_add():
    calculator = Calculator()
    result = calculator.add(2, 3)
    assert result == 5

def test_subtract():
    calculator = Calculator()
    result = calculator.subtract(5, 3)
    assert result == 2

def test_multiply():
    calculator = Calculator()
    result = calculator.multiply(4, 5)
    assert result == 20

def test_divide():
    calculator = Calculator()
    result = calculator.divide(10, 2)
    assert result == 5

def test_divide_by_zero():
    calculator = Calculator()
    with pytest.raises(ValueError):
        calculator.divide(10, 0)