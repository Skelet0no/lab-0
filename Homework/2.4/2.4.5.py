def answer(num):
    ans = 0
    for i in range(num):
        flag = False
        while True:
            match input():
                case "зайка":
                    flag = True
                case "ВСЁ":
                    break
        if flag:
            ans += 1
    return print(ans)


def main():
    num = int(input())
    answer(num)


if __name__ == "__main__":
    main()
