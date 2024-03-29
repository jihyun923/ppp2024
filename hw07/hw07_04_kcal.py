def total_calorie(fruits, fruits_calorie_dic):
    total_calorie = 0
    for fruit, gram in fruits.items():
        total_calorie += fruits_calorie_dic[fruit]/100 * gram
    print(f"총 칼로리는 {total_calorie}입니다.")

def main():
    fruits = {"딸기": 300, "한라봉": 150, "바나나": 140}
    fruits_calorie_dic = {"딸기": 34, "한라봉": 50, "바나나": 77}
    total_calorie(fruits, fruits_calorie_dic)

if __name__ == "__main__":
    main()