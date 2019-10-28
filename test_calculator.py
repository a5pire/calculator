from operations import Operations
from print_results import PrintResults
from get_numbers import GetNumbers


class TestOperations:

    def test_addition(self):
        add_positive_ints = Operations(36, 45)
        add_negative_ints = Operations(-5, -9)
        add_positive_and_negative_ints = Operations(10, -8)
        add_positive_floats = Operations(42.0, 5.3)
        add_negative_floats = Operations(-85.6, -37.9)
        add_positive_and_negative_floats = Operations(54.1, -12.2)

        assert round(add_positive_ints.addition(), 2) == 81
        assert round(add_negative_ints.addition(), 2) == -14
        assert round(add_positive_and_negative_ints.addition(), 2) == 2
        assert round(add_positive_floats.addition(), 2) == 47.3
        assert round(add_negative_floats.addition(), 2) == -123.5
        assert round(add_positive_and_negative_floats.addition(), 2) == 41.9

    def test_subtraction(self):
        subtract_positive_ints = Operations(42, 7)
        subtract_negative_ints = Operations(-13, -5)
        subtract_positive_and_negative_ints = Operations(12, -3)
        subtract_positive_floats = Operations(19.5, 7.9)
        subtract_negative_floats = Operations(-69.4, -51.7)
        subtract_positive_and_negative_floats = Operations(82.2, -24.6)

        assert round(subtract_positive_ints.subtraction(), 2) == 35
        assert round(subtract_negative_ints.subtraction(), 2) == -8
        assert round(subtract_positive_and_negative_ints.subtraction(), 2) == 15
        assert round(subtract_positive_floats.subtraction(), 2) == 11.6
        assert round(subtract_negative_floats.subtraction(), 2) == -17.7
        assert round(subtract_positive_and_negative_floats.subtraction(), 2) == 106.8

    def test_multiplication(self):
        multiply_positive_ints = Operations(9, 6)
        multiply_negative_ints = Operations(-26, -72)
        multiply_positive_and_negative_ints = Operations(12, -21)
        multiply_positive_floats = Operations(51.3, 3.6)
        multiply_negative_floats = Operations(-18.9, -34.1)
        multiply_positive_and_negative_floats = Operations(19.2, -35.8)

        assert round(multiply_positive_ints.multiplication(), 2) == 54
        assert round(multiply_negative_ints.multiplication(), 2) == 1872
        assert round(multiply_positive_and_negative_ints.multiplication(), 2) == -252
        assert round(multiply_positive_floats.multiplication(), 2) == 184.68
        assert round(multiply_negative_floats.multiplication(), 2) == 644.49
        assert round(multiply_positive_and_negative_floats.multiplication(), 2) == -687.36

    def test_division(self):
        divide_positive_ints = Operations(9, 3)
        divide_negative_ints = Operations(-36, -6)
        divide_positive_and_negative_ints = Operations(24, -6)
        divide_positive_floats = Operations(47.8, 22.5)
        divide_negative_floats = Operations(-62.3, -14.7)
        divide_positive_and_negative_floats = Operations(16.4, -8.8)
        divide_zero_by_zero = Operations(0, 0)

        assert round(divide_positive_ints.division(), 2) == 3
        assert round(divide_negative_ints.division(), 2) == 6
        assert round(divide_positive_and_negative_ints.division(), 2) == -4
        assert round(divide_positive_floats.division(), 2) == 2.12
        assert round(divide_negative_floats.division(), 2) == 4.24
        assert round(divide_positive_and_negative_floats.division(), 2) == -1.86
        assert divide_zero_by_zero.division() == f"You can't divide zero by zero, that's just ludicrous!"


class TestPrinting:

    def test_printing(self):
        add_result = 36
        subtract_result = 42
        multiply_result = 64
        divide_result = 7
        add_printer = PrintResults(add_result)
        subtract_printer = PrintResults(subtract_result)
        multiply_printer = PrintResults(multiply_result)
        divide_printer = PrintResults(divide_result)

        assert add_printer.printed_string() == 'The result is 36'
        assert subtract_printer.printed_string() == 'The result is 42'
        assert multiply_printer.printed_string() == 'The result is 64'
        assert divide_printer.printed_string() == 'The result is 7'


class TestGetNumbers:

    def test_get_operator(self, monkeypatch):
        monkeypatch.setattr('builtins.input', lambda x: 'a')
        operator = GetNumbers()
        user_operation = operator.get_operator()
        assert user_operation == 'a'

        monkeypatch.setattr('builtins.input', lambda x: 's')
        operator = GetNumbers()
        user_operation = operator.get_operator()
        assert user_operation == 's'

        monkeypatch.setattr('builtins.input', lambda x: 'm')
        operator = GetNumbers()
        user_operation = operator.get_operator()
        assert user_operation == 'm'

        monkeypatch.setattr('builtins.input', lambda x: 'd')
        operator = GetNumbers()
        user_operation = operator.get_operator()
        assert user_operation == 'd'

    def test_get_x(self, monkeypatch):
        monkeypatch.setattr('builtins.input', lambda x: '9')
        operator = GetNumbers()
        number = operator.get_x()
        assert number == 9

        monkeypatch.setattr('builtins.input', lambda x: '-25')
        operator = GetNumbers()
        number = operator.get_x()
        assert number == -25

    def test_get_y(self, monkeypatch):
        monkeypatch.setattr('builtins.input', lambda x: '100')
        operator = GetNumbers()
        number = operator.get_y()
        assert number == 100

        monkeypatch.setattr('builtins.input', lambda x: '-42')
        operator = GetNumbers()
        number = operator.get_y()
        assert number == -42
