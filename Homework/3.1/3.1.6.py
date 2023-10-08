def answer(n):
    ans = 0
    for i in range(n):
        phrase = input()
        ans += phrase.count("зайка")
    print(ans)


def main():
    n = int(input())
    answer(n)


if __name__ == "__main__":
    main()
