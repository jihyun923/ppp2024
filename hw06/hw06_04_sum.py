def sum_n(n):
    total = 0
    for i in range(n):
        total = total + (i + 1)
    return total

def main():
    n = int(input("1부터 몇까지의 수를 더할까요?"))
    print(f"1부터 {n}까지 합은 {sum_n(n)}입니다.")

if __name__ == "__main__":
    main()