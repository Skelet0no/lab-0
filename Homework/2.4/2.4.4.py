def answer(num):
    ans = 0
    for i in range(num):
        ans += sum(list(map(int, ''.join(input()))))
    return print(ans)


def main():
    num = int(input())
    answer(num)


if __name__ == "__main__":
    main()
