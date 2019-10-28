#!/usr/bin/env python3

from operations import Operations
from get_numbers import GetNumbers
from print_results import PrintResults


def main():

    while True:

        user_operation = GetNumbers()
        operator = user_operation.get_operator()

        get_x = GetNumbers()
        x = get_x.get_x()

        get_y = GetNumbers()
        y = get_y.get_y()

        if operator == 'a':
            add = Operations(x, y)
            add_result = round(add.addition(), 2)
            add_print = PrintResults(add_result)
            print(add_print.printed_string())
            print()

        elif operator == 's':
            subtract = Operations(x, y)
            sub_result = round(subtract.subtraction(), 2)
            sub_print = PrintResults(sub_result)
            print(sub_print.printed_string())
            print()

        elif operator == 'm':
            multiply = Operations(x, y)
            multiply_result = round(multiply.multiplication(), 2)
            multiply_print = PrintResults(multiply_result)
            print(multiply_print.printed_string())
            print()

        elif operator == 'd':
            divide = Operations(x, y)
            try:
                div_result = round(divide.division(), 2)
                div_print = PrintResults(div_result)
                print(div_print.printed_string())
            except TypeError:
                print(f"You can't divide zero by zero, that's just ludicrous!")
            print()


if __name__ == '__main__':
    main()
