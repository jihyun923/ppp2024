def c2f (temp_c):
    return temp_c * 9 / 5 + 32


def main():
    temp_c = int(input("섭씨 온도를 입력하세요."))
    print("{}C => {}F".format(temp_c,c2f(temp_c)))

if __name__ == "__main__":
    main()