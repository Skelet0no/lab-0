def answer(kg, rub, price1, price2):
    general_sum = kg * rub
    for kg1 in range(1, kg):
        kg2 = kg - kg1
        if kg1 * price1 + kg2 * price2 == general_sum:
            return print(kg1, kg2)


def main():
    kg = int(input())
    rub = int(input())
    price1 = int(input())
    price2 = int(input())
    answer(kg, rub, price1, price2)


if __name__ == "__main__":
    main()
