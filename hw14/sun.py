import requests
from hw14 import hw_submission

def download(filename, url):
    response = requests.get(url)
    if response.status_code == 200:
        with open(filename, "w", encoding="UTF-8") as f:
            f.write(response.text.replace("\r", ""))

def tmax(filename):
    max_tmax = 0
    with open(filename, "r", encoding="UTF-8") as f:
        lines = f.readlines()
        for line in lines[8:]:
            tokens = line.split(",")
            print(tokens)
            tmax = float(tokens[3])
            if max_tmax is None or tmax > max_tmax:
                max_tmax = tmax
    return max_tmax

def tmax_date(filename):
    max_tmax_date = 0
    max_tmax = 0
    with open(filename, "r", encoding="UTF-8") as f:
        lines = f.readlines()
        for line in lines[8:]:
            tokens = line.split(",")
            tmax = float(tokens[3])
            tmax_date = int(tokens[0])
            if max_tmax is None or tmax > max_tmax:
                max_tmax_date = tmax_date
    return max_tmax_date


def gap_max(filename):
    max_tdiff = 0
    with open(filename, "r", encoding="UTF-8") as f:
        lines = f.readlines()
        for line in lines[8:]:
            tokens = line.split(",")
            tdiff = float(tokens[4])
            if max_tdiff is None or tdiff > max_tdiff:
                max_tdiff = tdiff
    return max_tdiff

def gap_max_date(filename):
    max_tdiff = 0
    max_tdiff_date = 0
    with open(filename, "r", encoding="UTF-8") as f:
        lines = f.readlines()
        for line in lines[8:]:
            tokens = line.split(",")
            tdiff = float(tokens[4])
            tdiff_date = int(0)
            if max_tdiff is None or tdiff > max_tdiff:
                max_tdiff = tdiff
                max_tdiff_date = tdiff_date
    return max_tdiff, max_tdiff_date

#왜 오류가 뜨는지 모르겠습니다...
def main():
    URL = 'https://data.kma.go.kr/stcs/grnd/downloadGrndTaList.do?fileType=csv&pgmNo=70&menuNo=432&serviceSe=F00101&stdrMg=99999&startDt=19040101&endDt=20240422&taElement=MIN&taElement=AVG&taElement=MAX&stnGroupSns=&selectType=1&mddlClssCd=SFC01&dataFormCd=F00501&dataTypeCd=standard&startDay=19040101&startYear=190%BC&stnId=146&areaId=&gFontSize='
    filename = "ta_20240429021144.csv"
    download(filename, URL)

    hw_submission.submit("김지현", tmax(filename), tmax_date(filename), gap_max(filename), gap_max_date(filename))

if __name__ == '__main__':
    main()