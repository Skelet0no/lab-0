nums = []


def add_number(num):
    nums.append(num)


def get_sum():
    return " + ".join([str(i) for i in nums]) + f" = {sum(nums)}"
