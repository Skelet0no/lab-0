def answer(num):
    if num <= 1:
        return print("NO")
    for i in range(2, num // 2 + 1):
        if num % i == 0:
            return print("NO")
    return print("YES")


def main():
    num = int(input())
    answer(num)


if __name__ == "__main__":
    main()
