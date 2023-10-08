def answer(phrase):
    ans = ""
    for i in phrase:
        ans += i
    if ans == ans[::-1]:
        print("YES")
    else:
        print("NO")


def main():
    phrase = input().lower().split(" ")
    answer(phrase)


if __name__ == "__main__":
    main()
