def answer(price, weight, wallet):
    print(wallet - (price * weight))


def main():
    price = int(input())
    weight = int(input())
    wallet = int(input())
    answer(price, weight, wallet)


if __name__ == "__main__":
    main()
