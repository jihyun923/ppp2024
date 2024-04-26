import requests

def day_rainfall(data):
    day = 0
    lines = data.strip().split("\n")
    for line in lines[1:]:
        tokens = line.split(",")
        day_rainfall = float(tokens[9])
        if day_rainfall >= 5:
            day += 1
    return day

def main():
    URL = "https://api.taegon.kr/stations/146/?sy=2020&ey=2020&format=csv"
    res = requests.get(URL)
    res.encoding = "UTF-8"
    data = res.text

    rainy_days = day_rainfall(data)

    print(f"2020년 강수량이 5mm 이상인 날은 {rainy_days}일입니다.")

if __name__ == '__main__':
    main()