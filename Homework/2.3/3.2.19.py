def answer():
    right = 1000
    left = 0
    while True:
        middle = round((right + left) / 2)
        print(middle)
        hint = input()
        if hint == "Угадал!":
            return
        if hint == "Меньше":
            right = middle - 1
        else:
            left = middle + 1


def main():
    answer()


if __name__ == "__main__":
    main()
