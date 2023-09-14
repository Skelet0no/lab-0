def answer(count, phrase):
    print(f'Я больше никогда не буду писать "{phrase}"!\n' * count)


def main():
    count = int(input())
    phrase = input()
    answer(count, phrase)


if __name__ == "__main__":
    main()
