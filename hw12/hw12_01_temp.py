def max_day(filename):
    max_diff_temp = {}
    with open(filename) as f:
        lines = f.readlines()
        for line in lines[1:]:
            tokens = line.split(",")
            year = int(tokens[0])
            month = int(tokens[1])
            day = int(tokens[2])
            tmax = float(tokens[3])
            tmin = float(tokens[5])
            temp_diff = tmax - tmin
            if year not in max_diff_temp or temp_diff > max_diff_temp[year][0]:
                max_diff_temp[year] = (temp_diff, f"{year},{month},{day}")
    return max_diff_temp


def main():
    max_diff_per_year = max_day("hw12/weather(146)_2001-2022.csv")
    for year, (temp_diff, data) in max_diff_per_year.items():
        print(f"년도별 최대 일교차: [{data}], {temp_diff:.1f}C")

if __name__ =="__main__":
    main()