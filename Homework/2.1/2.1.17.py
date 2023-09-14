def answer(purchased_products, last_purchase):
    print(purchased_products + int(last_purchase, 2))


def main():
    purchased_products = int(input())
    last_purchase = input()
    answer(purchased_products, last_purchase)


if __name__ == "__main__":
    main()
