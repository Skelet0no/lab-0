def node(a, b):
    while b:
        a, b = b, a % b
    return a


def gcd(*nums):
    ans = nums[0]
    for i in range(1, len(nums)):
        ans = node(ans, nums[i])
    return ans
