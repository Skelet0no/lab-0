def answer(num):
    return print("YES" if num == num[::-1] else "NO")


def main():
    num = input()
    answer(num)


if __name__ == "__main__":
    main()
