class Calculator:
    """Controller class for Model CalcProcessor and View CalcUI"""
    @staticmethod
    def run_menu():
        while True:
            CalcUI.display_menu()
            menu_arg = CalcUI.get_menu_arg()
            if menu_arg is None:
                print("Invalid argument")
                continue
            if menu_arg == 5:
                exit()

            operands = CalcUI.get_operands()
            if operands is None:
                print("Invalid operand")
                continue

            try:
                result = CalcProcessor.run_calc(menu_arg, operands[0], operands[1])
                CalcUI.display_result(result)
            except ZeroDivisionError:
                print("Zero division!!!")


class CalcProcessor:

    @staticmethod
    def run_calc(operation, arg1, arg2):
        if operation == 1:
            return CalcProcessor.plus(arg1, arg2)
        elif operation == 2:
            return CalcProcessor.minus(arg1, arg2)
        elif operation == 3:
            return CalcProcessor.multiply(arg1, arg2)
        elif operation == 4:
            return CalcProcessor.division(arg1, arg2)

    @staticmethod
    def plus(a, b):
        return a + b

    @staticmethod
    def minus(a, b):
        return a - b

    @staticmethod
    def multiply(a, b):
        return a * b

    @staticmethod
    def division(a, b):
        return a / b


class CalcUI:
    @staticmethod
    def display_menu():
        print("1. +")
        print("2. -")
        print("3. *")
        print("4. /")
        print("5. exit")

    @staticmethod
    def display_result(result):
        print("Result: " + str(result))

    @staticmethod
    def get_menu_arg():
        try:
            return int(input(">: "))
        except:
            return None

    @staticmethod
    def get_operands():
        try:
            a = int(input("operand 1: "))
            b = int(input("operand 2: "))
            return [a, b]
        except:
            return None


if __name__ == "__main__":
    Calculator.run_menu()
