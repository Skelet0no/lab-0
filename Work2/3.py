def find_pair(*numbers, div=6):
    ans = [0, 0]
    teku, pred = 0, 0
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if (numbers[i] + numbers[j]) % div == 0:
                if numbers[i] + numbers[j] > pred:
                    teku, pred = j, numbers[i] + numbers[j]
                    ans = [numbers[i], numbers[j]]
                elif numbers[i] + numbers[j] == pred and j > teku:
                    teku, pred = j, numbers[i] + numbers[j]
                    ans = [numbers[i], numbers[j]]
    return tuple(ans)


numbers = [41, 56, 54, 6, 31, 81, 77, 83, 86, 15]
result = find_pair(*numbers, div=3)
print(*result)
