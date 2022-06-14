import pytest
from app.calculator import Calculator


class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_multiply_calculate_correctly(self):
        assert self.calc.multiply(4, 3) == 12

    def test_division_calculate_correctly(self):
        assert self.calc.division(4, 2) == 2

    def test_subtraction_calculate_correctly(self):
        assert self.calc.subtraction(4, 1) == 3

    def test_adding_calculate_correctly(self):
        assert self.calc.adding(4, 3) == 7
