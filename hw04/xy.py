x = int(input("x의 좌표값을 입력하세요."))
y = int(input("y의 좌표값을 입력하세요."))

if x > 0 and y > 0 :
    print("({},{}), 입력한 좌표는 제1사분면입니다.".format(x,y))
elif x < 0 and y > 0 :
    print("({},{}), 입력한 좌표는 제2사분면입니다.".format(x,y))
elif x < 0 and y < 0 :
    print("({},{}), 입력한 좌표는 제3사분면입니다.".format(x,y))
elif x > 0 and y < 0 :
    print("({},{}), 입력한 좌표는 제4사분면입니다.".format(x,y))
elif x == 0 and y == 0 :
    print("(0,0), 입력한 좌표는 원점입니다.")
elif x == 0 :
    print("입력한 좌표는 y선 위에 있습니다.")
elif y == 0 :
    print("입력한 좌표는 x선 위에 있습니다.")
    quit()