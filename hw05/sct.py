import math

print("라디안\t\t사인\t\t코사인\t\t탄젠트")
for i in range(0, 361, 15):
    r = i * (math.pi / 180)
    s = math.sin(r)
    c = math.cos(r)
    if i % 90 == 0:
        t = "Undefined"
    else:
        t =round(math.tan(r),4)
#포맷 함수로 소수점 조절하려 했는데 오류가 떠서 탄젠트만 round 함수를 썼습니다.
    print(f"{i}\t\t{s:.4f}\t\t{c:.4f}\t\t{t}")