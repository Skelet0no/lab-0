def answer(n):
    last_hash = 0
    ans = -1
    for i in range(n):
        bn = int(input())
# сдвигаем элементы по разрядам с помощью деления на 256, как при нахождении десятков, сотен, единиц и т.д.
        hn = bn % 256
        rn = (bn // 256) % 256
        mn = bn // 256 ** 2
        hashe = (37 * (mn + rn + last_hash)) % 256
        if hashe != hn or hashe > 100:
            ans = i
            break
        last_hash = hashe
    if ans != -1:
        return print(ans)   
    return print(-1)


def main():
    n = int(input())
    answer(n)


if __name__ == "__main__":
    main()
