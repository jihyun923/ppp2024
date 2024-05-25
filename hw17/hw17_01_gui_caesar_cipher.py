from tkinter import *

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

def caesar_decode(text:str, shift:int) -> str:
    result = ""
    for alp in text:
        if 'D' <= alp <= 'Z':
            result += chr((ord(alp) - shift))
        elif 'A' <= alp <= 'C':
            result += chr((ord(alp) + 23))
        elif 'd' <= alp <= 'z':
            result += chr((ord(alp) - shift))
        elif 'a' <= alp <= 'c':
            result += chr((ord(alp) + 23))
        else:
            result += alp
    return result

def encode_text():
    text = input_text.get()
    encoded_text = caesar_encode(text, 3)
    result_text.delete(1.0, END)
    result_text.insert(END, encoded_text)

def decode_text():
    text = input_text.get()
    decoded_text = caesar_decode(text, 3)
    result_text.delete(1.0, END)
    result_text.insert(END, decoded_text)

tk = Tk()
tk.geometry("500x200")
tk.title("Caesar Cipher")

input_text = Entry(tk)
input_text.grid(row=0, column=0, padx=10, pady=10)

encode_button = Button(tk, text="Encode", command=encode_text)
encode_button.grid(row=0, column=1, padx=10, pady=10)

decode_button = Button(tk, text="Decode", command=decode_text)
decode_button.grid(row=0, column=2, padx=10, pady=10)

result_text = Text(tk, height=4, width=50)
result_text.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

tk.mainloop()