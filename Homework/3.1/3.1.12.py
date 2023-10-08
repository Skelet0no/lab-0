def answer(num):
    ans = ["Манная", "Гречневая", "Пшённая", "Овсяная", "Рисовая"]
    for i in range(num):
        print(ans[(i % 5)])


def main():
    num = int(input())
    answer(num)


if __name__ == "__main__":
    main()
