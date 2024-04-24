import requests

url = "http://api.taegon.kr/stations/146/?sy=2022&ey=2022&format=csv"

filename = "./lec08/weather_146_2022.csv"

#파일이없으면다운받아라
if not os.path.exists(filename):
    with open(filename, "w") as f:
        res = requests.get(url)
        f.write(res.text)