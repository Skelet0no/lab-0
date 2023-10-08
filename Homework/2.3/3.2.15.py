def answer(num):
    ans = 0
    for i in range(num):
        phrase = input()
        if "зайка" in phrase:
            ans += 1
    return print(ans)


def main():
    num = int(input())
    answer(num)


if __name__ == "__main__":
    main()
