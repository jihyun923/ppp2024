def sumifs(filename):
    total = 0
    with open(filename) as f:
        lines = f.readlines()
        for line in lines[1:]:
            tokens = line.split(",")
            month = int(tokens[1])
            if 6 <= month <= 8:
                rainfall = float(tokens[9])
                total += rainfall
    return total

def main():
    total_rainfall = sumifs("hw11/weather(146)_2022-2022.csv")

    print(f"여름철 6,7,8월 총 강수량은 {total_rainfall:.1f}입니다.")


if __name__ =="__main__":
    main()