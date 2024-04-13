def temperature(filename):
    #연 평균 기온
    total_temperature = 0
    day = 0
    with open(filename, encoding='utf-8') as f:
        lines = f.readlines()
        for line in lines[1:]:
            tokens = line.split(",")
            tmax = float(tokens[3])
            tmin = float(tokens[5])
            day_temperature = (tmin + tmax) / 2
            total_temperature += day_temperature
            day += 1
        return total_temperature / day

def day_rainfall(filename):
    # 5mm 이상 강우일수
    day = 0
    with open(filename, encoding='utf-8') as f:
        lines = f.readlines()
        for line in lines[1:]:
            tokens = line.split(",")
            day_rainfall = float(tokens[9])
            if day_rainfall >= 5:
                day += 1
    return day

def rainfall(filename):
    #총 강우량
    results = []
    with open(filename, encoding='utf-8') as f:
        lines = f.readlines()
        for line in lines[1:]:
            tokens = line.split(",")
            rainfall = float(tokens[9])
            results.append(rainfall)
    return sum(results)

def main():
    tem = temperature("hw10/weather(146)_2022-2022.csv")
    day_rain = day_rainfall("hw10/weather(146)_2022-2022.csv")
    rain = rainfall("hw10/weather(146)_2022-2022.csv")

    print(f"2022년 연 평균 기온은 {tem:.2f}입니다.")
    print(f"강수량이 5mm 이상인 강우일수는 {day_rain}일입니다.")
    print(f"2022년도 총 강우량은 {rain:.2f}입니다.")

if __name__ == "__main__":
    main()