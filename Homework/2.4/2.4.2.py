def answer(num):
    for el1 in range(1, num + 1):
        for el2 in range(1, num + 1):
            print(f"{el2} * {el1} = {el1 * el2}")


def main():
    num = int(input())
    answer(num)


if __name__ == "__main__":
    main()
