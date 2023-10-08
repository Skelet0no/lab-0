def answer(num):
    dicti = {}
    ans = 0
    for i in range(num):
        name = input()
        number = input()
        dicti[sum(list(map(int, ''.join(number))))] = name
        ans = max(ans, sum(list(map(int, ''.join(number)))))
    print(dicti[ans])


def main():
    num = int(input())
    answer(num)


if __name__ == "__main__":
    main()
