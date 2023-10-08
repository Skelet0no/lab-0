def answer(num):
    num = list(map(int, ''.join(num)))
    print("YES" if max(num) + min(num) == (sum(num) - max(num) - min(num)) * 2 else "NO")


def main():
    num = input()
    answer(num)


if __name__ == "__main__":
    main()
