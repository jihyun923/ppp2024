from tkinter import *

def get_chosung(text):
    CHOSUNG_LIST = ['ㄱ', 'ㄲ', 'ㄴ', 'ㄷ', 'ㄸ', 'ㄹ', 'ㅁ', 'ㅂ', 'ㅃ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅉ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']

    chosung = []

    for guelja in text:
        chosung.append(CHOSUNG_LIST[(ord(guelja) - ord('가')) // 588])

    return chosung

def check_answer():
    global trial
    x = answer_entry.get()
    if x not in hidden_answer:
        trial -= 1
        result_label.config(text=f"정답이 아닙니다. 목숨 {trial}개 남았습니다.")
    else:
        result_label.config(text="정답입니다!")
        check_button.config(state=DISABLED)

    if trial <= 0:
        result_label.config(text=f"정답을 맞히지 못했습니다. 정답은 '{hidden_answer}'입니다.")
        check_button.config(state=DISABLED)

hidden_answer = "스마트팜"
problem = get_chosung(hidden_answer)
trial = 3

root = Tk()
root.title("초성 퀴즈 게임")
root.geometry("300x200")

chosung_label = Label(root, text=f"주어진 초성: {''.join(problem)}")
chosung_label.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

answer_label = Label(root, text="정답 입력:")
answer_label.grid(row=1, column=0, padx=10, pady=10)
answer_entry = Entry(root)
answer_entry.grid(row=1, column=1, padx=10, pady=10)

check_button = Button(root, text="확인", command=check_answer)
check_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

result_label = Label(root, text="결과가 여기에 표시됩니다.")
result_label.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()