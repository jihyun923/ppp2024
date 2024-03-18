import math

x1 = 0
y1 = 0
x2 = 3
y2 = 5

dist = math.sqrt((x2-x1)**2 + (y2-y1)**2)

if dist > 1 :
    print("거리는 {:.1f}입니다.".format(dist))
else :
    print("거리가 너무 가깝습니다.")
#:.1f 원하는 자리수만큼 출력
#:.숫자f