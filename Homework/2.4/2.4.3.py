def answer(num):
    n = 1
    for el1 in range(1, num + 1):
        for el2 in range(0, el1):
            print(n, end=" ")
            n += 1
            if n > num:
                break
        if n > num:
            break

        print()


def main():
    num = int(input())
    answer(num)


if __name__ == "__main__":
    main()
