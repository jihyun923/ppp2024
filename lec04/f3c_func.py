##!주차 코드
temp_f = 100
temp_c = (temp_f - 32) * 5 / 0
print("{}F => {}C".format(temp_f, temp_c))

##4주차 코드
def f2c (temp_f):
    return (temp_f - 32) * 5 / 9

temp_f = 100
print("{}F => {}C",format(temp_f, f2c(temp_f)))