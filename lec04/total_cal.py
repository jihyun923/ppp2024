fruit = input("과일: ")
f_gram = int(input("양(g): "))

cal = {"한라봉":0.5, "딸기": 0.34, "바나나": 0.77, "사과": 0.57, "배": 0.45}

if "한라봉" in fruit:
    total_cal = cal["한라봉"]* f_gram
elif "딸기" in fruit:
    total_cal = cal["딸기"]* f_gram
elif "바나나" in fruit:
    total_cal = cal["바나나"]* f_gram
elif "사과" in fruit:
    total_cal = cal["사과"]* f_gram
elif "배" in fruit:
    total_cal = cal["배"]* f_gram

if fruit not in cal:
    print("알 수 없는 과일")
else:
    print("총 칼로리: {:.0f}".format(total_cal))
