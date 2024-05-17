def toggle_text(text: str) -> str:
    result = ""
    for alp in text:
        if 'A' <= alp <= 'Z':
            result += chr(ord(alp) + 32)
        elif 'a' <= alp <= 'z':
            result += chr(ord(alp) - 32)
        else:
            result += alp
    return result

def main():
    input_text = input("알파벳을 입력하세요.")
    result = toggle_text(input_text)
    print(result)

if __name__ == "__main__":
    main()