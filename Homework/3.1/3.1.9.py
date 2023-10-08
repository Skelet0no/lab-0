def answer():
    ans = []
    while True:
        phrase = input()
        if phrase == "":
            break
        if phrase.split("#")[0] != "":
            ans.append(phrase.split("#")[0])
    for i in ans:
        print(i)


def main():
    answer()


if __name__ == "__main__":
    main()
