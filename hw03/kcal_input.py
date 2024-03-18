s = int(input("딸기의 무게를 입력하세요."))
b = int(input("바나나의 무게를 입력하세요."))
h = int(input("한라봉의 무게를 입력하세요."))

s_k = s * 0.34 
b_k = b * 0.77
h_k = h * 0.5

print("딸기 {}g은 {}kcal, 바나나 {}g은 {}kcal, 한라봉 {}g은 {}kcal입니다.".format(s,s_k,b,b_k,h,h_k))