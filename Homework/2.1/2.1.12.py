def answer(num1, num2):
    num1, num2 = max(num1, num2), min(num1, num2)
    num1, num2 = str(num1), str(num2)
    a = len(num1) - len(num2)
    ans = ""
    for i in range(1, len(num2) + 1):
        ans += str((int(num1[-i]) + int(num2[-i])) % 10)
    print(str(num1)[:a] + ans[::-1])


def main():
    number1 = int(input())
    number2 = int(input())
    answer(number1, number2)


if __name__ == "__main__":
    main()
