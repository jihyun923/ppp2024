import math

print("라디안\t\t사인\t\t코사인\t\t탄젠트")
for i in range(0, 361, 15):
    r = i * (math.pi / 180)
    s = math.sin(r)
    c = math.cos(r)
    if i % 90 == 0:
        t = "Undefined"
    else:
        t = round(math.tan(r), 4)
    print(f"{i}\t\t{:.f4}\t\t{:.f4}\t\t{t}".format(s,c))