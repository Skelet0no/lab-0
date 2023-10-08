def answer(phrase, repeats):
    print((phrase + "\n") * repeats)


def main():
    phrase = input()
    repeats = int(input())
    answer(phrase, repeats)


if __name__ == "__main__":
    main()
