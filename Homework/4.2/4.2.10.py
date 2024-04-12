def secret_replace(text, **kwargs):
    for i in kwargs:
        kwargs[i] = [kwargs[i], 0]
    ans = ""
    for i in text:
        if i not in kwargs:
            ans += i
            continue
        ans += kwargs[i][0][kwargs[i][1] % len(kwargs[i][0])]
        kwargs[i][1] += 1
    return ans
