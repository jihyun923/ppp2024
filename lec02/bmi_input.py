# weight = 60
# height_cm = 170

# height_cm = input("키를 입력하세요.")
# height_cm = int(height_cm)
# weight = input("몸무게를 입력하세요.")
# weight = int(weight)

height_cm = int(input("키를 입력하세요."))
weight = int(input("몸무게를 입력하세요."))

bmi = weight / (height_cm ** 2)
print("키가 {}cm, 몸무게가 {}kg이면, BMI는 {}입니다.".format(height_cm,weight,bmi))



