from tkinter import *

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

def on_toggle():
    input_str = input_text.get()
    toggled_str = toggle_text(input_str)
    output_text.delete(0, END)
    output_text.insert(0, toggled_str)

tk = Tk()
tk.geometry('500x300')
tk.title("Toggle Case")

Label(tk, text="입력 텍스트:").grid(row = 0, column = 0, padx = 10, pady = 5)
input_text = Entry(tk, width = 50)
input_text.grid(row = 0, column = 1, padx = 10, pady = 5)

btn = Button(tk, text="대소 변환", command=on_toggle)
btn.grid(row = 1, column = 0, columnspan=2, padx=10, pady=10)

Label(tk, text = "출력 텍스트:").grid(row = 2, column = 0, padx = 10, pady = 5)
output_text = Entry(tk, width = 50)
output_text.grid(row = 2, column = 1, padx = 10, pady = 5)

tk.mainloop()