from math import sqrt


def answer(x, y):
    if ((x + 7) * (x - 5)) / 4 <= y <= 0:
        return print("Опасность! Покиньте зону как можно скорее!")
    if x ** 2 + y ** 2 <= 25 and y >= 0 and x >= 0:
        return print("Опасность! Покиньте зону как можно скорее!")
    if 5 >= y >= 0 and x <= 0 and ((5 * x + 35) / 3 >= y):
        return print("Опасность! Покиньте зону как можно скорее!")
    if x ** 2 + y ** 2 <= 100:
        return print("Зона безопасна. Продолжайте работу.")
    return print("Вы вышли в море и рискуете быть съеденным акулой!")


def main():
    x, y = float(input()), float(input())
    answer(x, y)


if __name__ == "__main__":
    main()
