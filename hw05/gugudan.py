dan = int(input("원하는 구구단 단수를 입력하세요."))

for i in range(1,10):
    print(f"{dan} * {i} = {dan * i:2d}")
#i+=1 누적이나 합계에 관한 식에 쓸 수 있음
#i+1 = n으로 써서 치환해서 사용 가능