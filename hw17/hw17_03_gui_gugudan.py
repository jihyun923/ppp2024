import tkinter as tk
import random

def gugudan():
    random_num = random.randint(1, 9)
    random_num2 = random.randint(1, 9)
    answer = random_num * random_num2
    quiz_text = f"{random_num} * {random_num2} = "
    return quiz_text, answer

def check_answer():
    global score, total_quiz
    try:
        user_answer = int(answer_entry.get())
    except ValueError:
        result_label.config(text="올바른 숫자를 입력하세요.")
        return

    if user_answer == answer:
        result_label.config(text="정답입니다!", fg="green")
        score += 1
    else:
        result_label.config(text=f"틀렸습니다. 정답은 {answer}입니다.", fg="red")

    total_quiz += 1
    score_label.config(text=f"점수: {score}/{total_quiz}")
    ask_next_question()

def ask_next_question():
    global answer
    quiz_text, answer = gugudan()
    quiz_label.config(text=quiz_text)
    answer_entry.delete(0, tk.END)
    result_label.config(text="")

def end_game():
    result_label.config(text=f"수고하셨습니다. 총 {total_quiz}문제 중 {score}개 맞히셨습니다.", fg="blue")

# GUI 설정
root = tk.Tk()
root.title("구구단 퀴즈")
root.geometry("400x300")

quiz_label = tk.Label(root, text="")
quiz_label.pack()

answer_entry = tk.Entry(root)
answer_entry.pack()

check_button = tk.Button(root, text="확인", command=check_answer)
check_button.pack()

score_label = tk.Label(root, text="점수: 0/0")
score_label.pack()

result_label = tk.Label(root, text="", fg="green")
result_label.pack()

end_button = tk.Button(root, text="종료", command=end_game)
end_button.pack()

score = 0
total_quiz = 0
ask_next_question()

root.mainloop()