def answer(num):
    max_len = 0
    for i in range(1, num + 1):
        if max_len + i >= num:
            break
        max_len += i
    last_str = 0
    for i in range(max_len + 1, num + 1):
        last_str += len(str(i)) + 1
    n = 1
    for i in range(1, num + 1):
        lst = ""
        for j in range(i):
            lst += str(n) + " "
            n += 1
            if n > num:
                return print(f"{lst: ^{last_str}}")
        print(f"{lst: ^{last_str}}")


def main():
    num = int(input())
    answer(num)


if __name__ == "__main__":
    main()
