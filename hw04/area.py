import math

r = int(input("반지름의 길이를 입력하세요."))
area = math.pi * r ** 2
c = 2 * math.pi * r

print("반지름의 길이가 {}인 원의 둘레는 {:.1f}이고, 면적은 {:.2f}입니다.".format(r,c,area))