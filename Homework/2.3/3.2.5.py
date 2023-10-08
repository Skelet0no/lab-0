def answer():
    ans = 0
    while True:
        price = float(input())
        if price == 0:
            return print(ans)
        if price >= 500.00:
            ans += price * 0.9
        else:
            ans += price


def main():
    answer()
    

if __name__ == "__main__":
    main()
