from math import gcd


def answer(a, b):
    print(gcd(a, b))


def main():
    a = int(input())
    b = int(input())
    answer(a, b)


if __name__ == "__main__":
    main()
