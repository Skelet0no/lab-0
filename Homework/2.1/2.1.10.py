def answer(name, number):
    print(f"Группа №{number // 100}.\n{number % 10}. {name}.\nШкафчик: {number}.\nКроватка: {number // 10 % 10}.")


def main():
    name = input()
    number = int(input())
    answer(name, number)


if __name__ == "__main__":
    main()
