def answer(lenn, n):
    for i in range(n):
        phrase = input()
        if phrase[:lenn] != phrase:
            print(phrase[:lenn - 3] + "...")
        else:
            print(phrase[:lenn])


def main():
    lenn = int(input())
    n = int(input())
    answer(lenn, n)


if __name__ == "__main__":
    main()
