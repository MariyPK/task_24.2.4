import pytest

from app.calculator import Calculator

class TestCalc:
    def setup(self):
        self.calculator = Calculator

    def test_multiply_success(self):
        assert self.calculator.multiply(self,2,5) == 10

    def test_division_success(self):
        assert self.calculator.division(self,12,2) == 6

    def test_subtraction_success(self):
        assert self.calculator.subtraction(self,100,40) == 60

    def test_adding_success(self):
        assert self.calculator.adding(self,1,1) == 2

    def teardown(self):
        print("Выполнение метода Teardown")