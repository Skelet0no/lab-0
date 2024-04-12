def answer():
    while True:
        phrase = input()
        match phrase:
            case "Три!":
                print("Ёлочка, гори!")
                break
            case _:
                print("Режим ожидания...")


def main():
    answer()


if __name__ == "__main__":
    main()
