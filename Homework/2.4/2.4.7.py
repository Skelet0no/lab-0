def answer(num):
    for i in range(num):
        for j in range(3 + i, 0, -1):
            print(f"До старта {j} секунд(ы)")
        print(f"Старт {i + 1}!!!")


def main():
    num = int(input())
    answer(num)


if __name__ == "__main__":
    main()
