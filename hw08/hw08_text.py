def text2list(input_text):
    tokens = input_text.split()
    nums = []
    for token in tokens:
        nums.append(int(token))
    return nums

def average(nums):
    return sum(nums) / len(nums)

def median(nums):
    nums.sort()
    n = len(nums)
    if n % 2 == 0:
        return (nums[n//2 - 1] + nums[n//2]) / 2
    else:
        return nums[n//2]

def main():
    input_text = "5 10 3 4 7 9"
    nums = text2list(input_text)
    nums.sort()
    print("주어진 리스트는", nums)
    print("평균값은 {:.1f}".format(average(nums)))
    print("중앙값은 {}".format(median(nums)))
    print("최솟값은 {}".format(min(nums)))
    print("최댓값은 {}".format(max(nums)))

if __name__ == "__main__":
    main()