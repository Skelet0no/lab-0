def answer(numbers):
    degree = int(input())
    print(*[i ** degree for i in numbers])


def main():
    numbers = list(map(int, input().split()))
    answer(numbers)


if __name__ == "__main__":
    main()
