#어디서 잘못된지 모르겠습니다.ㅜㅜ

def first_gdd(filename):
    first_day = {}
    with open(filename) as f:
        lines = f.readlines()
        for line in lines[1:]:
            tokens = line.split(",")
            temp = float(tokens[4])
            year = int(tokens[0])
            month = int(tokens[1])
            day = int(tokens[2])
            if 4 <= month:
                eff_temp = temp - 5
                if eff_temp > 200:
                    if year not in first_day:
                        first_day[year] = (f"{year}/{month}/{day}")
    return first_day

def main():
    first_day = first_gdd("hw12/weather(146)_2001-2022.csv")

    for year, date in first_day.items():
        print(f"해마다 적산온도가 200이 넘는 최초일은: {date}입니다.")

if __name__ =="__main__":
    main()