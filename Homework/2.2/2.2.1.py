def answer():
    print("Как Вас зовут?")
    name = input()
    print(f"Здравствуйте, {name}!\nКак дела?")
    mood = input()
    match mood:
        case "хорошо":
            print("Я за вас рада!")
        case "плохо":
            print("Всё наладится!")


def main():
    answer()


if __name__ == "__main__":
    main()
