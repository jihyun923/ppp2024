def average(nums):
    total = 0
    for num in nums:
        total += num
    return total / len(nums)

def main():
    x = [5, 8, 19, 2, 18]
    print(f"이 수들의 평균은 {average(x)}입니다.")

if __name__ == "__main__":
    main()