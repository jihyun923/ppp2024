temp_c = 30
temp_f = (temp_c) * 9 / 5 + 32
print("{}C => {}F".format(temp_c,temp_f))
temp_c = 0
temp_f = (temp_c) * 9 / 5 + 32
print("{}C => {}F".format(temp_c,temp_f))

weight = 60
height = 170
bmi = (weight)/((height/100) ** 2)
print("키가 {}cm이고 몸무게가 {}kg이면 BMI = {}입니다.".format(height,weight,bmi))

r = 4
pi = 3.14
area = pi * r ** 2
print("반지름의 길이가 {}cm인 원의 면적은 {}입니다.".format(r,area))

bottom = 5
upper = 3
height = 4
area = (bottom + upper) * height / 2
print("밑변의 길이가 {}cm, 윗변의 길이가 {}cm, 높이가 {}cm인 사다리꼴의 면적은 {}입니다.".format(bottom,upper,height,area))