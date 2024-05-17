def caesar_encode(text:str, shift:int) -> str:
    result = ""
    for alp in text:
        if 'A' <= alp <= 'W':
            result += chr((ord(alp) + shift))
        elif 'X' <= alp <= 'Z':
            result += chr((ord(alp) - 23))
        elif 'a' <= alp <= 'w':
            result += chr((ord(alp) + shift))
        elif 'x' <= alp <= 'z':
            result += chr((ord(alp) - 23))
        else:
            result += alp
    return result


def main():
    input_text = input("문자열을 입력하세요.")
    result = caesar_encode(input_text, 3)
    print(result)

if __name__== "__main__":
    main()