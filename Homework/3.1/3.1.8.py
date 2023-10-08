def answer(n):
    ans = []
    for i in range(n):
        phrase = input()
        if "зайка" in phrase:
            ans.append(len(phrase.split("зайка")[0]) + 1)
        else:
            ans.append("Заек нет =(")
    for i in ans:
        print(i)


def main():
    n = int(input())
    answer(n)


if __name__ == "__main__":
    main()
