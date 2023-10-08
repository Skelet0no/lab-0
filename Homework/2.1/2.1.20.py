def answer(kg, rub, price1, price2):
    general_sum = kg * rub
    print(int(((price2 - rub) * kg) / (price2 - price1)), int(kg - (((price2 - rub) * kg) / (price2 - price1))))


def main():
    kg = int(input())
    rub = int(input())
    price1 = int(input())
    price2 = int(input())
    answer(kg, rub, price1, price2)


if __name__ == "__main__":
    main()
