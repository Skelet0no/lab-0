def answer(product, price, weight, wallet):
    print(f"Чек\n{product} - {weight}кг - {price}руб/кг\nИтого: {price * weight}руб\n"
          f"Внесено: {wallet}руб\nСдача: {wallet - (price * weight)}руб")


def main():
    product = input()
    price = int(input())
    weight = int(input())
    wallet = int(input())
    answer(product, price, weight, wallet)


if __name__ == "__main__":
    main()
