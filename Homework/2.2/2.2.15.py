def answer(num1, num2):
    print(max(num1 + num2) + str((sum(list(map(int, num1 + num2))) - int(min(num1 + num2)) - int(max(num1 + num2))) % 10)
          + min(num1 + num2))


def main():
    num1 = list(''.join(input()))
    num2 = list(''.join(input()))
    answer(num1, num2)


if __name__ == "__main__":
    main()
