def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


def answer(numbers):
    ans = numbers[0]
    for i in range(1, len(numbers)):
        ans = gcd(ans, numbers[i])
    print(ans)


def main():
    numbers = list(map(int, input().split()))
    answer(numbers)


if __name__ == "__main__":
    main()
