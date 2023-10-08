def answer():
    ans = dict()
    while True:
        phrase = input()
        if phrase == "ФИНИШ":
            break
        for i in phrase.lower():
            if i not in ans:
                ans[i] = 1
            else:
                ans[i] += 1
    print(max(ans, key=ans.get))


def main():
    answer()


if __name__ == "__main__":
    main()
