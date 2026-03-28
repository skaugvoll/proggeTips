from src.example_1 import example_1
from src.example_2 import example_2

hb = "\n" + "=" * 50 + "\n"


def main():
    print(hb)
    example_1()
    print(hb)
    example_2()
    print(hb)


if __name__ == "__main__":
    main()
