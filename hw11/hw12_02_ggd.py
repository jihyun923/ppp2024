def gdd(filename):
    total_gdd = {}
    with open(filename) as f:
        lines = f.readlines()
        for line in lines[1:]:
            tokens = line.split(",")
            temp = float(tokens[4])
            year = int(tokens[0])
            month = int(tokens[1])
            if 5 <= month <= 9:
                eff_temp = temp - 5
                if eff_temp < 0:
                    eff_temp = 0
                if year in total_gdd:
                    total_gdd[year] += eff_temp
                else:
                    total_gdd[year] = eff_temp
    return total_gdd

def main():
    total_gdd = gdd("weather(146)_2001-2022.csv")

    for year, gdd_season in total_gdd.items():
        print(f"{year}년 적산온도: {gdd_season:.1f}C입니다.")

if __name__ =="__main__":
    main()