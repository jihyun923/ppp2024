import requests
import matplotlib.pyplot as plt
import os

def download(filename, URL):
    if not os.path.exists(filename):
        with open(filename, "w", encoding="utf-8-sig") as f:
            res = requests.get(URL)
            f.write(res.text.replace("\r", ""))

def weather(filename):
    tmax_list = []
    tmin_list = []
    avg_list = []
    years = []

    with open(filename, encoding="UTF-8") as f:
        lines = f.readlines()
        for line in lines[8:]:
            tokens = line.strip().split(",")
            if len(tokens) != 5:
                continue
            if tokens[4] == '':
                continue
            tmax = float(tokens[4])
            tmin = float(tokens[3])
            avg = float(tokens[2])
            year = tokens[0]
            tmax_list.append(tmax)
            tmin_list.append(tmin)
            avg_list.append(avg)
            years.append(year)
    return tmax_list, tmin_list, avg_list, years

def main():
    filename = "ta_20240528161818.csv"
    URL = f"https://data.kma.go.kr/stcs/grnd/downloadGrndTaList.do?fileType=csv&pgmNo=70&menuNo=432&serviceSe=F00101&stdrMg=99999&startDt=19800101&endDt=20231231&taElement=MIN&taElement=AVG&taElement=MAX&stnGroupSns=&selectType=1&mddlClssCd=SFC01&dataFormCd=F00501&dataTypeCd=standard&startDay=19800101&startYear=1980&endDay=20231231&endYear=2023&startMonth=01&endMonth=12&sesnCd=0&txtStnNm=%EC%A0%84%EC%A3%BC&stnId=146&areaId=&gFontSize=%22"
    download(filename, URL)

    plt.rcParams['font.family'] = ['NanumGothic', 'sans-serif']
    plt.rcParams['axes.unicode_minus'] = False

    tmax_list, tmin_list, avg_list, years = weather(filename)

    plt.plot(years, tmax_list, color = 'r', label = '평균최고기온')
    plt.plot(years, tmin_list, color = 'b', label = "평균최저기온")
    plt.plot(years, avg_list, color = 'g', label = "평균기온")

    plt.ylabel = ("기온")
    plt.xlabel("년도")
    plt.xticks(fontsize=6)
    plt.legend()
    plt.savefig("./weather_temp.png")


if __name__ == "__main__":
    main()