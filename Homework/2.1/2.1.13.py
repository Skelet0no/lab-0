def answer(kids, candies):
    print(candies // kids)
    print(candies % kids)


def main():
    kids = int(input())
    candies = int(input())
    answer(kids, candies)


if __name__ == "__main__":
    main()
