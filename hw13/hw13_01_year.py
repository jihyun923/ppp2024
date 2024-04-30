import requests

def temperature(data):
    # 연 평균 기온
    total_temperature = 0
    day = 0
    lines = data.strip().split("\n")
    for line in lines[1:]:
        tokens = line.split(",")
        tavg = float(tokens[4])
        total_temperature += tavg
        day += 1
    return total_temperature / day

def main():
    URL = "https://api.taegon.kr/stations/146/?sy=2020&ey=2020&format=csv"
    res = requests.get(URL)
    res.encoding = "UTF-8"
    data = res.text

    avg_temperature = temperature(data)

    print(f"2020년 연 평균 기온은 {avg_temperature:.1f}도입니다.")

if __name__ == '__main__':