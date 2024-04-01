def average(nums):
    # return sum(nums)/len(nums)
    total = 0
    count = 0
    for num in nums:
        total += num
        count += 1

    return total / count

def main():
    nums = [3, 5, 10, 15, 7]
    print(f"주어진 리스트의 평균은 {average(nums):.1f}입니다.")

if __name__== "__main__":
    main()

#2

def average(nums):
  return 0

def main():
    nums = [3, 5, 10, 15, 7]
    print(f"주어진 리스트의 평균은 {average(nums):.1f}입니다.")
#여기서 average(num)의 값은 0 return에서 0을 출력.

if __name__== "__main__":
    main()