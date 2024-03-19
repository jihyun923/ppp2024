#무게에 따른 과일의 칼로리

kcal = {"한라봉": 50, "딸기": 34, "바나나": 77, "키위": 54, "파인애플": 50, "레몬": 17}


h = int(input("한라봉의 무게를 입력하세요."))
s = int(input("딸기의 무게를 입력하세요."))
b = int(input("바나나의 무게를 입력하세요."))
k = int(input("키위의 무게를 입력하세요."))
p = int(input("파인애플의 무게를 입력하세요."))
l = int(input("레몬의 무게를 입력하세요."))

h_kcal = kcal["한라봉"]/100 * h
s_kcal = kcal["딸기"]/100 * s
b_kcal = kcal["바나나"]/100 * b
k_kcal = kcal["키위"]/100 * k
p_kcal = kcal["파인애플"]/100 * p
l_kcal = kcal["레몬"]/100 * l

total_kcal = h_kcal + s_kcal + b_kcal + k_kcal + p_kcal + l_kcal

print("섭취한 총 칼로리는 {}입니다.".format(total_kcal))