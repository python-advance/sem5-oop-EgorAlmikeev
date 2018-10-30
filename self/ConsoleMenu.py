class ConsoleMenu:

    menu_dict: dict
    menu_description: str

    def __init__(self, menu_description, menu_dict: dict):
        """
        menu_dict key have to be a description of menu item
        menu_dict value have to be a function reference
        """
        self.menu_dict = menu_dict
        self.menu_description = menu_description

    @staticmethod
    def get_argument():
        return int(input("set: "))

    def display_menu(self):
        print(self.menu_description)
        i = 1
        for key in self.menu_dict:
            print(str(i) + ") " + str(key))
            i += 1
        print(str(i) + ") " + "exit")

    def exec(self):
        while True:
            print("\n")
            self.display_menu()

            try:
                argument = self.get_argument()
            except (TypeError, ValueError):
                print("Failed to convert argument to int")
                continue
            except KeyboardInterrupt:
                exit()

            if argument not in range(1, len(self.menu_dict) + 2):
                print("Argument out of range")
                continue

            if argument == len(self.menu_dict) + 1:
                exit()

            list(self.menu_dict.values())[argument - 1]()


def func1():
    print("Im func1")


def func2():
    print("Im func2")


def func3():
    print("Im func3")


if __name__ == "__main__":
    menu = ConsoleMenu(
        "This is test menu",
        {
            "call func1": func1,
            "call func2": func2,
            "call func3": func3,
        }
    )
    menu.exec()

