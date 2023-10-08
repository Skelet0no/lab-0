def answer(product, price, weight, wallet):
    len_str = 35    # длинна чека (================Чек================)
    print(f'''================Чек================
Товар:{' ' * (len_str - len("Товар:") - len(product))}{product}
Цена:{' ' * (len_str - len("Цена:") - len("кг * руб/кг") - len(str(price) + str(weight)))}{weight}кг * {price}руб/кг
Итого:{' ' * (len_str - len("Итого:") - len("руб") - len(str(price * weight)))}{price * weight}руб
Внесено:{' ' * (len_str - len("Внесено:") - len("руб") - len(str(wallet)))}{wallet}руб
Сдача:{' ' * (len_str - len("Сдача:") - len("руб") - len(str(wallet - (price * weight))))}{wallet - (price * weight)}руб
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
