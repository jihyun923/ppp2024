def average(nums):
    return sum(nums) / len(nums)

def median(nums):
    sorted_nums = sorted(nums)
    return sorted_nums[len(nums) // 2]

def read_list_from_file(filename):
    data = []
    with open(filename) as f:
        lines = f.readlines()
        for line in lines:
            tokens = line.split()
            for token in tokens:
                value = int(token)
                data.append(value)
    return data

def main():
    nums = read_list_from_file("hw09/number.txt")

    print("주어진 리스트는", nums)
    print("리스트에 있는 숫자의 총 개수는 {}".format(len(nums)))
    print("평균값은 {:.1f}".format(average(nums)))
    print("중앙값은 {}".format(median(nums)))
    print("최솟값은 {}".format(min(nums)))
    print("최댓값은 {}".format(max(nums)))
    print(f"리스트의 마지막 값은 {nums[-1]}")

if __name__ == "__main__":
    main()