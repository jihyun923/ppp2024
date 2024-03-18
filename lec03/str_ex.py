text = input("영어단어를 입력하세요.")

print('입력한 문자는"{}"입니다.'.format(text))
print(len(text))
#글자수 출력 함수 len
print(text.upper())
#대문자로 변환해 주는 함수 upper

print(5 * 20)
print("5" * 20)
#"" 따옴표 안의 글자는 문자로 인식

print(text[:3])
#첫 3글자 출력
print(text[-2:])
#마지막 2글자 출력
print(text[4])
#인덱스 계산은 첫 글자는 0부터 셈
#단어에서 문자 하나 출력하는 것

#문자열 뒤집기
print(text[::-1])