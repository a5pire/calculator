import sys


class GetNumbers:

    @staticmethod
    def get_operator():

        choice = ['a', 's', 'm', 'd']

        while True:
            user_operation = input(f'Choose your operation: [a]dd, [s]ubtract, [m]ultiply, [d]ivide, [q]uit: ').lower()

            if user_operation == 'q':
                print(f'Good Bye!')
                sys.exit()
            elif user_operation not in choice:
                print('Illegal choice, try again: [a], [s], [m], [d] or [q]')
                print()
            else:
                break   # break out of loop and continue with the calculation (user input is accepted)
        return user_operation

    @staticmethod
    def get_x():
        while True:
            x = input(f'Choose the first number: ')
            try:
                val_x = float(x)
                return float(val_x)
            except ValueError:
                print(f'Illegal numeric character (only numbers 0-9)')
                print()

    @staticmethod
    def get_y():
        while True:
            y = input(f'Choose the second number: ')
            try:
                val_y = float(y)
                return float(val_y)
            except ValueError:
                print(f'Illegal numeric character (only numbers 0-9)')
                print()
