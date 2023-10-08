def answer(num):
    ans = 0
    for _ in range(num):
        n = input()
        if n == n[::-1]:
            ans += 1
    print(ans)


def main():
    num = int(input())
    answer(num)


if __name__ == "__main__":
    main()
