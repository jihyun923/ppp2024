import tkinter as tk
import random

#입력값이 정수가 아닐 경우를 if문으로 작성하고 싶은데 모르겠습니다.
def level1_quiz():
    num = random.randint(1,10)
    text = int(input_answer.get())
    if text == num:
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, "정답!")
    else:
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, f"땡! 정답은 {num}")
    if text < 0 or text > 10:
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, "땡! 1부터 10 사이의 수를 입력하세요.")

def level2_quiz():
    num = random.randint(1,50)
    text = int(input_answer.get())
    if text == num:
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, "정답!")
    else:
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, f"땡! 정답은 {num}")
    if text < 0 or text > 50:
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, "땡! 1부터 50 사이의 수를 입력하세요.")

def level3_quiz():
    num = random.randint(1,100)
    text = int(input_answer.get())
    if text == num:
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, "정답!")
    elif text != num:
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, f"땡! 정답은 {num}")
    if text < 0 or text > 100:
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, "땡! 1부터 100 사이의 수를 입력하세요.")



window = tk.Tk()
window.title("숫자 맞히기 게임")
window.geometry("600x300")

#규격 조정하는 게 어려워염...
label = tk.Label(window, text="Level 1은 1부터 10까지의 수, level 2는 1부터 50까지, level 3은 1부터 100까지의 수 중 맞히는 게임 ", fg="blue")
label.grid(row=0, columnspan=6, padx=30, pady=10)

input_answer = tk.Entry(window, width=40)
input_answer.grid(row=1, columnspan=5, padx=30, pady=10)

button1 = tk.Button(window, text="level 1 도전", fg="green", command=level1_quiz)
button1.grid(row=2, column=1, padx=1, pady=10)

button2 = tk.Button(window, text="level 2 도전", fg="green", command=level2_quiz)
button2.grid(row=2, column=2, padx=1, pady=10)

button3 = tk.Button(window, text="level 3 도전", fg="green", command=level3_quiz)
button3.grid(row=2, column=3, padx=1, pady=10)

result_text = tk.Text(window, width=40, height=5)
result_text.grid(row=4, columnspan=5, padx=30, pady=10)

tk.mainloop()