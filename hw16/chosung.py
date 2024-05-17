def get_chosung(text):
    CHOSUNG_LIST = ['ㄱ', 'ㄲ', 'ㄴ', 'ㄷ', 'ㄸ', 'ㄹ', 'ㅁ', 'ㅂ', 'ㅃ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅉ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']

    chosung = []

    for guelja in text:
        chosung.append(CHOSUNG_LIST[(ord(guelja) - ord('가'))//588])

    return chosung


def main():
    hidden_answer = "스마트팜"
    problem = get_chosung(hidden_answer)
    trial = 3

    while True:
        x = input(f"주어진 초성은 '{''.join(problem)}'입니다. 목숨 {trial}개")
        if x not in hidden_answer:
            trial -= 1
            print(f"정답이 아닙니다. 목숨 {trial}개")
        else:
            print("정답입니다.")
            break

        if trial <= 0:
            print("정답을 맞히지 못했습니다. 정답은 '스마트팜'입니다.")
            break

if __name__ == "__main__":
    main()