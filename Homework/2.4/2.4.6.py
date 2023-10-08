def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


def answer(num):
    lst = [int(input()) for _ in range(num)]
    ans = lst[0]
    for i in range(1, num):
        ans = gcd(lst[i], ans)
    print(ans)


def main():
    num = int(input())
    answer(num)


if __name__ == "__main__":
    main()
