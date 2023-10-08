from math import sqrt


def answer(a, b, c):
    if a == 0:
        return print("Infinite solutions")
    if b ** 2 - 4 * a * c >= 0:
        x1 = "%.2f" % round((-b - sqrt(b ** 2 - 4 * a * c)) / (2 * a), 2)
        x2 = "%.2f" % round((-b + sqrt(b ** 2 - 4 * a * c)) / (2 * a), 2)
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
    if a == "Infinite" or b == "Infinite" or c == "Infinite":
        return print("Infinite solutions")
    answer(float(a), float(b), float(c))


if __name__ == "__main__":
    main()
