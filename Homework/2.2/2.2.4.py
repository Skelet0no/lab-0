def answer(petya, vasya, tolya):
    first_place = "Петя" if petya > vasya and petya > tolya else "Вася" if vasya > petya and vasya > tolya else "Толя"
    third_place = "Петя" if petya < vasya and petya < tolya else "Вася" if vasya < petya and vasya < tolya else "Толя"
    second_place = "ПетяВасяТоля"
    second_place = second_place.replace(first_place, "")
    second_place = second_place.replace(third_place, "")
    print(f"1. {first_place}\n2. {second_place}\n3. {third_place}")


def main():
    petya = int(input())
    vasya = int(input())
    tolya = int(input())
    answer(petya, vasya, tolya)


if __name__ == "__main__":
    main()
