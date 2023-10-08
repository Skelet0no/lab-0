def answer(dima_to_petya, dima_to_vasya):
    petya = 7 - 3 + 2 + dima_to_petya
    vasya = 6 + 3 + 5 - 2 + dima_to_vasya
    print("Петя" if petya >= vasya else "Вася")


def main():
    dima_to_petya = int(input())
    dima_to_vasya = int(input())
    answer(dima_to_petya, dima_to_vasya)


if __name__ == "__main__":
    main()
