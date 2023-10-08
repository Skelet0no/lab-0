def answer(a, b, c):
    sides = [a, b, c]
    if (sum(sides) - (max(sides) + min(sides))) ** 2 + min(sides) ** 2 == max(sides) ** 2:
        print("100%")
    elif (sum(sides) - (max(sides) + min(sides))) ** 2 + min(sides) ** 2 < max(sides) ** 2:
        print("велика")
    else:
        print("крайне мала")


def main():
    a = int(input())
    b = int(input())
    c = int(input())
    answer(a, b, c)


if __name__ == "__main__":
    main()
