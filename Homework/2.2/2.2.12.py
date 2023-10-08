def answer(num1, num2, num3):
    nums = [num1, num2, num3]
    print("YES" if min(nums) + (sum(nums) - max(nums) - min(nums)) > max(nums) else "NO")


def main():
    num1 = int(input())
    num2 = int(input())
    num3 = int(input())
    answer(num1, num2, num3)


if __name__ == "__main__":
    main()
