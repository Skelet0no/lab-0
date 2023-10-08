def answer(num):
    for i in "123456789":
        if i in num:
            for j in "987654321":
                if j in num:
                    num1, num2 = num.copy(), num.copy()
                    num1.pop(num1.index(i))
                    num2.pop(num2.index(j))
                    print(i + str(min(num1)), end=" ")
                    print(j + str(max(num2)))
                    return


def main():
    num = list(''.join(input()))
    answer(num)


if __name__ == "__main__":
    main()
