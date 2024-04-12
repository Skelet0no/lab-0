from math import sqrt


def answer(a, b, c):
    if a == 0 and b == 0 and c == 0:
        return print("Infinite solutions")
    if a == 0 and b == 0:
        return print("No solution")
    if a == 0 and b != 0:
        return print(format((-c) / b, '.2f'))
    if b == 0 and a != 0:
        return print(format(sqrt((-c) / a)), '.2f')
    if (b ** 2) - (4 * a * c) >= 0:
        x1 = format((-b - sqrt((b ** 2) - (4 * a * c))) / (2 * a), '.2f')
        x2 = format((-b + sqrt((b ** 2) - (4 * a * c))) / (2 * a), '.2f')
        x1, x2 = min(x1, x2), max(x1, x2)
        if x1 == x2:
            print(x1)
        else:
            print(x1, x2)
    else:
        print("No solution")


def main():
    a = input()
    b = input()
    c = input()
    answer(float(a), float(b), float(c))


if __name__ == "__main__":
    main()
