def answer(petya, vasya, tolya):
    print("Петя" if petya > vasya and petya > tolya else "Вася" if vasya > petya and vasya > tolya else "Толя")


def main():
    petya = int(input())
    vasya = int(input())
    tolya = int(input())
    answer(petya, vasya, tolya)


if __name__ == "__main__":
    main()
