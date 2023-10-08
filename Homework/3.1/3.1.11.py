def answer(num):
    ans = []
    for i in range(num):
        phrase = input()
        ans.append(phrase)
    search = input()
    for i in ans:
        if search.lower() in i.lower():
            print(i)


def main():
    num = int(input())
    answer(num)


if __name__ == "__main__":
    main()
