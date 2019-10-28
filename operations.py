
class Operations:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def addition(self):
        return self.x + self.y

    def subtraction(self):
        return self.x - self.y

    def multiplication(self):
        return self.x * self.y

    def division(self):
        if self.x == 0 and self.y == 0:
            try:
                self.x / self.y
            except ZeroDivisionError:
                return f"You can't divide zero by zero, that's just ludicrous!"
        else:
            return self.x / self.y
