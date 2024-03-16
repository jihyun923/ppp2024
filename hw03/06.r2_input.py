import math

x1 = int(input("x1의 값을 입력하세요."))
y1 = int(input("y1의 값을 입력하세요."))
x2 = int(input("x2의 값을 입력하세요."))
y2 = int(input("y2의 값을 입력하세요."))

d = math.sqrt(((x2-x1) ** 2) + ((y2-y1) ** 2))

print("x1의 값이 {}, y1의 값이 {}, x2의 값이 {}, y2의 값이 {}인 점 사이의 거리는 {}입니다.".format(x1,y1,x2,y2,d))