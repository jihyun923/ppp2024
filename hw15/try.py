def number():
    numbers = []
    try:
        num = int(input("숫자를 입력하세요."))
        if num % 1 == 0:
            numbers.append(num)
        if len(numbers) > 1:
            numbers.append(num)
            numbers.split(",")
    except ValueError:
            print("유효한 정수를 입력하세요.")
    return numbers
def average(numbers):
    if len(numbers) == 0:
        return 0
    aver = sum(numbers) / len(numbers)
    return aver

def main():
    numbers = number()
    avg = average(numbers)
    if len(numbers) > 0:
        print(f"입력된 값은 {numbers}입니다. 총 {len(numbers)}개의 자연수가 입력되었고, 평균은 {avg}입니다.")

if __name__ == '__main__':
    main()