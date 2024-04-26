import requests

def rainfall(data):
    total_rain = 0
    lines = data.strip().split("\n")
    for line in lines[1:]:
        tokens = line.split(",")
        rainfall = float(tokens[9])
        total_rain += rainfall
    return total_rain

def main():
    URL = "https://api.taegon.kr/stations/146/?sy=2020&ey=2020&format=csv"
    res = requests.get(URL)
    res.encoding = "UTF-8"
    data = res.text

    total_rainfall = rainfall(data)

    print(f"2020년 총 강수량은 {total_rainfall:.1f}mm입니다.")

if __name__ == '__main__':
    main()
