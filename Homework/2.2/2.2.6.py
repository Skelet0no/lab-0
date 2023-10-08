def answer(year):
    exception = [100, 200, 300, 400, 800, 1200, 1600, 2000, 2400]
    print("YES" if (year % 4 == 0 and str(year)[:-3:-1] != '00' or year in exception) else "NO")


def main():
    year = int(input())
    answer(year)


if __name__ == "__main__":
    main()
