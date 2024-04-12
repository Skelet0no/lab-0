def answer(phrase1, phrase2, phrase3):
    phrase1 = [True if "зайка" in phrase1 else False, phrase1, len(phrase1)]
    phrase2 = [True if "зайка" in phrase2 else False, phrase2, len(phrase2)]
    phrase3 = [True if "зайка" in phrase3 else False, phrase3, len(phrase3)]
    ans = [0, "", 0]
    for i in [phrase1, phrase2, phrase3]:
        if i[0]:
            if ans == [0, "", 0]:
                ans = i
                continue
            for j in range(len(i[1])):
                if i[1][j] < ans[1][j]:
                    ans = i
                    break
                if i[1][j] > ans[1][j]:
                    break
    return print(*ans[1:])


def main():
    phrase1 = input()
    phrase2 = input()
    phrase3 = input()
    answer(phrase1, phrase2, phrase3)


if __name__ == "__main__":
    main()
