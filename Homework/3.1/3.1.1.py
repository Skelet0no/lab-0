def answer(repeats):
    ans = "YES"
    for i in range(repeats):
        phrase = input()
        if phrase[0] not in "абв":
            ans = "NO"
    print(ans)


def main():
    repeats = int(input())
    answer(repeats)


if __name__ == "__main__":
    main()
