height = int(input("키를 입력하세요."))
weight = int(input("몸무게를 입력하세요."))
bmi = weight / (height/100)**2

if 23 <= bmi <= 24.9 :
    print("키 {}cm, 몸무게 {}kg에 따른 bmi는 {}kg/㎡입니다. 비만 전단계입니다.".format(height,weight,bmi))
elif bmi <= 29.9 :
    print("키 {}cm, 몸무게 {}kg에 따른 bmi는 {}kg/㎡입니다. 1단계 비만입니다.".format(height,weight,bmi))
elif bmi <= 34.9 :
    print("키 {}cm, 몸무게 {}kg에 따른 bmi는 {}kg/㎡입니다. 2단계 비만입니다.".format(bheight,weight,bmi))
elif 35 <= bmi :
    print("키 {}cm, 몸무게 {}kg에 따른 bmi는 {}kg/㎡입니다. 3단계 비만입니다. 관리가 필요합니다.".format(height,weight,bmi))