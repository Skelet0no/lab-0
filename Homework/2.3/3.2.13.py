def answer(num):
    ans = "ЯЯЯЯЯЯЯ"
    for _ in range(num):
        name = input()
        for i in range(min(len(ans), len(name))):
            if ans[i] < name[i]:
                break
            if ans[i] == name[i]:
                continue
            ans = name
            break
    return print(ans)


def main():
    num = int(input())
    answer(num)


if __name__ == "__main__":
    main()
