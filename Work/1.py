num = int(input())
for _ in range(num):
    i = input()
    work = i.split("&")
    a, b, c = int(work[0]), int(work[1]), list(work[2])
    k = c[a::2]
    print("".join(k[:b:]))
