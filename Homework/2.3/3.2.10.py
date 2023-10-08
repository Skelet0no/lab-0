def answer():
    x, y = 0, 0
    while True:
        match input():
            case "СЕВЕР":
                y += int(input())
            case "ЮГ":
                y -= int(input())
            case "ВОСТОК":
                x += int(input())
            case "ЗАПАД":
                x -= int(input())
            case _:
                return print(y, x, sep="\n")


def main():
    answer()


if __name__ == "__main__":
    main()
