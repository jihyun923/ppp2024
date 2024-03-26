eat_fruits = ["한라봉", "딸기", "바나나", "사과"]
eat_grams = [50, 34, 77, 57]

eat_fruits_dic = {"한라봉": 50, "딸기": 34, "바나나": 77, "사과": 57}

cal = {"한라봉": 0.5, "딸기": 0.34, "바나나": 0.77, "사과":0.57}

total_cal = 0
idx = 0
for eat_fruit in eat_fruits:
    for fruit in cal:
        if eat_fruit == fruit:
            total_cal += cal[fruit] * eat_grams[idx]
    idx += 1

total_cal = 0
for eat_fruit, eat_gram in eat_fruits_dic.items():
    for fruit in cal:
        if eat_fruit == fruit:
            total_cal += cal[fruit] * eat_gram

print(f"총 칼로리는 {total_cal}입니다.")