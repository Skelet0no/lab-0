def answer(num):
    ans = ""
    for i in range(num):
        number = input()
        ans += str(max(list(map(int, ''.join(number)))))
    print(ans)


def main():
    num = int(input())
    answer(num)


if __name__ == "__main__":
    main()
