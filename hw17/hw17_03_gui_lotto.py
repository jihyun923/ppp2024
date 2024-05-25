import random
import tkinter as tk

def get_lotto():
    results = []

    while True:
        num = random.randint(1, 45)
        if num not in results:
            results.append(num)
        if len(results) == 6:
            return sorted(results)

def show_lotto():
    lotto_nums = get_lotto()
    result_label.config(text=str(lotto_nums))

root = tk.Tk()
root.title("로또 번호 생성기")
root.geometry("400x300")

frame = tk.Frame(root)
frame.pack(pady=20)

generate_button = tk.Button(frame, text="로또 번호 생성", command=show_lotto)
generate_button.pack(padx=10, pady=10)

result_label = tk.Label(root, text="")
result_label.pack(pady=10)

root.mainloop()