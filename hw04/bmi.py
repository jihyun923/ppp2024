height = int(input("키를 입력하세요."))
weight = int(input("몸무게를 입력하세요."))
bmi = weight / (height/100)**2

#좌항과 우항의 조건에 모두 만족해야 하기 때문에 and 필수
if bmi < 23:
    print("비만이 아닙니다.")
elif 23 <= bmi and bmi <= 24.9 :
    print("키 {}cm, 몸무게 {}kg에 따른 bmi는 {}kg/㎡입니다. 비만 전단계입니다.".format(height,weight,bmi))
elif bmi <= 29.9 :
    print("키 {}cm, 몸무게 {}kg에 따른 bmi는 {}kg/㎡입니다. 1단계 비만입니다.".format(height,weight,bmi))
elif bmi <= 34.9 :
    print("키 {}cm, 몸무게 {}kg에 따른 bmi는 {}kg/㎡입니다. 2단계 비만입니다.".format(height,weight,bmi))
elif 35 <= bmi :
    print("키 {}cm, 몸무게 {}kg에 따른 bmi는 {}kg/㎡입니다. 3단계 비만입니다. 관리가 필요합니다.".format(height,weight,bmi))