def answer(num):
    ans = []
    for i in range(num):
        numbers = int(input())
        ans.append(numbers)
    degree = int(input())
    for i in ans:
        print(i ** degree)


def main():
    num = int(input())
    answer(num)


if __name__ == "__main__":
    main()
