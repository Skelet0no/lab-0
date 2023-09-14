def answer(price, wallet):
    print(wallet - int(price, 2))


def main():
    price = input()
    wallet = int(input())
    answer(price, wallet)


if __name__ == "__main__":
    main()
