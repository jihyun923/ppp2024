import math

print("라디안\t\t사인\t\t코사인\t\t탄젠트")
for i in range(0, 361, 15):
    r = i * (math.pi / 180)
    s = round(math.sin(r), 4)
    c = round(math.cos(r), 4)
    if i % 90 == 0:
        t = "        Undefined"
    else:
        t = round(math.tan(r), 4)
    print(f"{i}\t\t{s}\t\t{c}\t\t{t}")