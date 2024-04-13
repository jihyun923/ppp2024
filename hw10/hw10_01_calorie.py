def total_calorie(fruits_eat, fruits_cal_dic):
    return sum([gram * fruits_cal_dic[name] / 100
                for name, gram in fruits_eat.items()])

def read_calories(filename):
    database = {}
    with open(filename, encoding="utf-8") as f:
        lines = f.readlines()
        for line in lines[1:]:
            tokens = line.split(",")
            fruit_name = tokens[0]
            fruit_cal = int(tokens[1])
            database[fruit_name] = fruit_cal
    return database

def main():
    fruits_calorie_dic = read_calories("hw10/calorie_db.csv")
    fruits_name = input("과일 이름을 입력하세요.")
    fruits_gram = int(input("과일의 무게를 입력하세요."))

    fruits_eat = {fruits_name: fruits_gram}

    total = total_calorie(fruits_eat, fruits_calorie_dic)

    print(f"섭취한 과일: {fruits_name}, 무게: {fruits_gram}")
    print(f"총 섭취한 칼로리는 {total}입니다.")

if __name__ == "__main__":
    main()