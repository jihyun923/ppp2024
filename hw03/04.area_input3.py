bottom = int(input("사다리꼴의 밑변의 길이를 입력하세요."))
upper = int(input("사다리꼴의 윗변의 길이를 입력하세요."))
height = int(input("사다리꼴의 높이를 입력하세요."))

area = (bottom + upper) * height / 2
print("밑변의 길이가 {}이고 윗변의 길이가 {}, 높이가 {}인 사다리꼴의 면적은 {}입니다.".format(bottom,upper,height,area))