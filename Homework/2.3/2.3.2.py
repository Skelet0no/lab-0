def answer():
    ans = 0
    while True:
        phrase = input()
        ans += phrase.count("зайка")
        if phrase == "Приехали!":
            return print(ans)


def main():
    answer()


if __name__ == "__main__":
    main()
