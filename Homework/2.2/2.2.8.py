def answer(phrase):
    print("YES" if "зайка" in phrase else "NO")


def main():
    phrase = input()
    answer(phrase)


if __name__ == "__main__":
    main()
