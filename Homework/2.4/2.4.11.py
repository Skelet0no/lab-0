def answer(repeats):
    ans = 0
    for _ in range(repeats):
        num = int(input())
        flag = True
        if num <= 1:
            flag = False
        for i in range(2, num // 2 + 1):
            if num % i == 0:
                flag = False
                break
        if flag:
            ans += 1
    print(ans)


def main():
    repeats = int(input())
    answer(repeats)


if __name__ == "__main__":
    main()
