def merge_sort(spi):
    if len(spi) == 1:
        return spi
    a = merge_sort(spi[:len(spi) // 2])
    b = merge_sort(spi[len(spi) // 2:])
    res = []
    while len(a) > 0 and len(b) > 0:
        if a[0] >= b[0]:
            res.append(b[0])
            b.pop(0)
            continue
        res.append(a[0])
        a.pop(0)
    if len(a) > 0:
        res += a
    elif len(b) > 0:
        res += b
    return res


result = merge_sort([3, 2, 1, 2, 6, 8, 4, 7, 2, 9, 5])
print(result)
