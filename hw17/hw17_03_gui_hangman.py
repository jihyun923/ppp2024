import tkinter as tk

def update_shown_answer(shown_answer, hidden_answer, x):
    results = []

    for shown_text, hidden_text in zip(shown_answer, hidden_answer):
        if shown_text == "_":
            if x == hidden_text:
                results.append(x)
            else:
                results.append("_")
        else:
            results.append(shown_text)

    return "".join(results)


def check_input():
    global shown_answer, trial, hidden_answer
    x = input_entry.get()
    input_entry.delete(0, tk.END)

    if x in hidden_answer:
        shown_answer = update_shown_answer(shown_answer, hidden_answer, x)
        shown_label.config(text=shown_answer)
    else:
        trial -= 1
        trial_label.config(text=f"목숨: {trial}")

        if trial <= 0:
            result_label.config(text="정답을 맞히지 못했습니다.\n정답은 " + hidden_answer + "입니다.")
        else:
            result_label.config(text=f"입력하신 '{x}'는 정답에 없습니다.")

        if "_" not in shown_answer:
            result_label.config(text="축하합니다. 정답입니다.")

root = tk.Tk()
root.title("단어 맞추기 게임")
root.geometry("400x300")

frame = tk.Frame(root)
frame.pack(pady=20)

hidden_answer = "apple"
shown_answer = "_" * len(hidden_answer)
trial = 3

shown_label = tk.Label(root, text=shown_answer)
shown_label.pack()

trial_label = tk.Label(root, text=f"목숨: {trial}")
trial_label.pack()

input_entry = tk.Entry(root)
input_entry.pack()

check_button = tk.Button(root, text="확인", command=check_input)
check_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()