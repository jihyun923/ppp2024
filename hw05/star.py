height = int(input("삼각형의 높이를 입력하세요: "))

for i in range(height):
    print((" " * (height - i - 1)) + ("*" * (2 * i + 1)))