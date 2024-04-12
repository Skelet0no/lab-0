from sys import stdin
import json


def prost():
    spi = [i for i in range(1000000)]
    spi[1] = 0
    n = 2
    while n < 1000000:
        if spi[n] != 0:
            j = n * 2
            while j < 1000000:
                spi[j] = 0
                j += n
        n += 1
    return [i for i in spi if i != 0]


nums = []
ez_nums = prost()
ans = {}
for i in stdin:
    nums.append(int(i))
nums = list(set(nums))
for i in nums:
    for j in range(len(ez_nums)):
        if i % ez_nums[j] == 0:
            if ez_nums[j] in ans.keys():
                ans[ez_nums[j]].append(i)
            else:
                ans[ez_nums[j]] = [i]
for i in ans.keys():
    ans[i] = sorted(ans[i])

with open("result.json", "w", encoding="UTF-8") as out:
    json.dump(ans, out, ensure_ascii=False, indent=3)
