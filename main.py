# main.py

from module.mymodule import Greeter

def main():
    greeter = Greeter("Bob")
    print(greeter.greet())
    print(greeter.farewell())


if __name__ == "__main__":
    main()
