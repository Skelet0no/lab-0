def answer(num):
    ans = ""
    for _ in range(1000):
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                if ans == "":
                    ans += f"{i} "
                    num //= i
                    break
                ans += f"* {i} "
                num //= i
                break
    return print(ans + f"* {num}")


def main():
    num = int(input())
    answer(num)


if __name__ == "__main__":
    main()
