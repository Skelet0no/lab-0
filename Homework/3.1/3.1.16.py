def answer(lenn, n):
    for i in range(n):
        phrase = input()
        if lenn > 0:
            print(phrase[:lenn], end="")
            lenn -= len(phrase)
            if lenn < 0:
                print("...")
            else:
                print()


def main():
    lenn = int(input()) - 3
    n = int(input())
    answer(lenn, n)


if __name__ == "__main__":
    main()
