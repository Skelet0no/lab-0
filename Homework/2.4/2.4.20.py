letters = "0123456789"


def convert(num, base):
    ans = ""
    while num > 0:
        sys = num % base
        ans = letters[sys] + ans
        num //= base
    return ans


def answer(num):
    lst = []
    for base in range(2, 11):
        lst.append(sum(list(map(int, "".join(convert(num, base))))))
    return print(lst.index(max(lst)) + 2)


def main():
    num = int(input())
    answer(num)


if __name__ == "__main__":
    main()
