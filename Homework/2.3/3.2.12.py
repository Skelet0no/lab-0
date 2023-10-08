def answer(num):
    print(max(list(map(int, ''.join(num)))))


def main():
    num = input()
    answer(num)


if __name__ == "__main__":
    main()
