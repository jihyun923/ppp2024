def get_range_list(n):
    return list(range(1, n+1))

def main():
    n = int(input("몇까지 수를 나열할까요?"))
    print(get_range_list(n))

if __name__== "__main__":
    main()