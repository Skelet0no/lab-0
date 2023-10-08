from math import lcm


def answer(a, b):
    print(lcm(a, b))


def main():
    a = int(input())
    b = int(input())
    answer(a, b)


if __name__ == "__main__":
    main()
