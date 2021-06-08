class Calculator():
    def addition(self, x, y):
        return x+y

    def subtraction(self, x, y):
        return x-y

    def multiplication(self, x, y):
        return x*y

    def division(self, x, y):
        return x/y

    def power(self, x, y):
        return x**y


def action():
    if z == "+":
        print(run_calculator.addition(x, y))
    elif z == "-":
        print(run_calculator.subtraction(x, y))
    elif z == "*":
        print(run_calculator.multiplication(x, y))
    elif z == "/":
        try:
            run_calculator.division(x, y)
        except ZeroDivisionError:
            print("На ноль делить нельзя!")
    elif z == "**":
        try:
            run_calculator.power(x, y)
        except ZeroDivisionError:
            print("Нельзя возводить ноль в отрицательную степень!")


run_calculator = Calculator()


if __name__ == "__main__":
    while True:
        try:
            x = float(input("Введите 1 число: "))
            z = str(input("Введите действие(+, -, *, /, **): "))
            y = float(input("Введите 2 число: "))
        except:
            print("Введено не коректное значение!")
        action()
