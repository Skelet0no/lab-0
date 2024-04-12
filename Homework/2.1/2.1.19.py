def answer(product, price, weight, wallet):
    print(f'''================Чек================
Товар:{' ' * (35 - 6 - len(product))}{product}
Цена:{' ' * (35 - 5 - 11 - len(str(price) + str(weight)))}{weight}кг * {price}руб/кг
Итого:{' ' * (35 - 6 - 3 - len(str(price * weight)))}{price * weight}руб
Внесено:{' ' * (35 - 8 - 3 - len(str(wallet)))}{wallet}руб
Сдача:{' ' * (35 - 6 - 3 - len(str(wallet - (price * weight))))}{wallet - (price * weight)}руб
===================================
''')


def main():
    product = input()
    price = int(input())
    weight = int(input())
    wallet = int(input())
    answer(product, price, weight, wallet)


if __name__ == "__main__":
    main()
