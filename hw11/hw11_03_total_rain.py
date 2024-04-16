def rainfall(filename):
    total_rain = 0
    with open(filename) as f:
        lines = f.readlines()
        for line in lines[1:]:
            tokens = line.split(",")
            year = int(tokens[0])
            if 2021 <= year <= 2022:
                rainfall = float(tokens[9])
                total_rain += rainfall
    return total_rain


def main():
    total_rainfall = rainfall("hw11/weather(146)_2001-2022.csv")

    print(f"2021년과 2022년 총 강수량은 {total_rainfall:.1f}mm입니다.")

if __name__ == '__main__':
    main()