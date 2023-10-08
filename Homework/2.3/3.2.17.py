def answer(num):
    ans = ''
    for i in num:
        if int(i) % 2 != 0:
            ans += i
    return print(ans)


def main():
    num = input()
    answer(num)


if __name__ == "__main__":
    main()
