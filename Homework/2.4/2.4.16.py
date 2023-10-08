def answer(a, b):
    for i in range(1, a + 1):
        stroka = a - 1
        for j in range(1, a + 1):
            if j == a:
                print(f"{str(i * j): ^{b}}", end="")
                stroka += len(f"{str(i * j): ^{b}}")
                break
            print(f"{str(i * j): ^{b}}", end="|")
            stroka += len(f"{str(i * j): ^{b}}")
        print()
        if i != a:
            print("-" * stroka)


def main():
    a, b = int(input()), int(input())
    answer(a, b)


if __name__ == "__main__":
    main()
