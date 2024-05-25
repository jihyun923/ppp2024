import tkinter as tk
import time

def start_countdown():
    try:
        count = int(entry.get())
        if count < 1:
            raise ValueError("자연수를 입력하세요.")
    except ValueError as e:
        label.config(text=str(e))
        return

    def countdown():
        nonlocal count
        while count > 0:
            label.config(text=f"카운트다운... {count}")
            time.sleep(1)
            count -= 1
        label.config(text="Bomb!")

    countdown()

root = tk.Tk()
root.title("카운트다운 타이머")
root.geometry("300x150")

entry = tk.Entry(root)
entry.pack(pady=10)

button = tk.Button(root, text="시작", command=start_countdown)
button.pack(pady=10)

label = tk.Label(root, text="시간(초)을 입력하세요.")
label.pack(pady=10)

root.mainloop()