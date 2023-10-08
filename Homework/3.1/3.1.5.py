def answer(word):
    if word == word[::-1]:
        print("YES")
    else:
        print("NO")


def main():
    word = input()
    answer(word)


if __name__ == "__main__":
    main()
