#최장연속강우일수
def rainfall(filename):
    day = 0
    rain_day = []
    with open(filename) as f:
        lines = f.readlines()
        for line in lines[1:]:
            tokens = line.split(",")
            rainfall = float(tokens[9])
            if rainfall == 0:
                if day > 0:
                    rain_day.append(day)
                day = 0
            else:
                day += 1
    return max(rain_day)

def max_rainfall(filename):
    day = 0
    rain_day = []
    rain_event = []
    with open(filename) as f:
        lines = f.readlines()
        for line in lines[1:]:
            tokens = line.split(",")
            rainfall = float(tokens[9])
            if rainfall == 0:
                if day > 0:
                    rain_day.append(day)
                day = 0
            else:
                day += 1
                rain_event.append(rainfall)
    return max(rain_event)

def top_rank(filename):
    top_temps = []
    with open(filename) as f:
        lines = f.readlines()
        for line in lines[1:]:
            tokens = line.split(",")
            temperature = float(tokens[3])
            top_temps.append(temperature)
    top_temps.sort(reverse=True)
    return top_temps[:3]

def main():
    rainday = rainfall("hw11/weather(146)_2022-2022.csv")
    rain = max_rainfall("hw11/weather(146)_2022-2022.csv")
    rank = top_rank("hw11/weather(146)_2022-2022.csv")

    print(f"최장 연속 강우일수는 {rainday}일입니다.")
    print(f"최대 강우량은 {rain}mm입니다.")
    print(f"가장 더운 날 top3 기온은 {rank}입니다.")
if __name__ =="__main__":
    main()