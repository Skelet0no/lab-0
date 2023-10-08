def answer(num):
    for i in range(len(num)):
        number, count = num[i], 0
        if num[i] == num[i - 1]:
            continue
        for j in range(i, len(num)):
            if num[i] != num[j] or len(num) == j:
                print(number, count)
                break
            else:
                count += 1


def main():
    num = input() + "!"
    answer(num)


if __name__ == "__main__":
    main()
