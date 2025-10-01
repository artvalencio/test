# my_module.py

class Greeter:
    def __init__(self, name: str):
        self.name = name

    def greet(self) -> str:
        return f"Hello, {self.name}!"

    def farewell(self) -> str:
        return f"Goodbye, {self.name}!"


def main():
    """Example main for standalone execution"""
    greeter = Greeter("Alice")
    print(greeter.greet())
    print(greeter.farewell())


if __name__ == "__main__":
    main()
