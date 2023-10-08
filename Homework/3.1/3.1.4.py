def answer():
    while True:
        phrase = input()
        if phrase == "":
            break
        if phrase[:2] == "##" and phrase[-1:-4:-1] != "@@@":
            print(phrase[2:])
        elif phrase[-1:-4:-1] != "@@@":
            print(phrase)


def main():
    answer()


if __name__ == "__main__":
    main()
