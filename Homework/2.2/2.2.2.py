def answer(petya , vasya):
    print("Петя" if petya > vasya else "Вася")


def main():
    petya = int(input())
    vasya = int(input())
    answer(petya, vasya)


if __name__ == "__main__":
    main()
