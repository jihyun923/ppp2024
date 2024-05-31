import tkinter as tk

def caesar_encode(text:str, shift:int) -> str:
    result = ""
    for alp in text:
        if 'a' <= alp <= 'z':
            result += chr((ord(alp) - ord('a') + shift) % 26 + ord('a'))
        elif 'A' <= alp <= 'Z':
            result += chr((ord(alp) - ord('A') + shift) % 26 + ord('A'))
        else:
            result += alp

    return result

def caesar_decode(text:str, shift:int) -> str:
    result = ""
    for alp in text:
        if 'a' <= alp <= 'z':
            result += chr((ord(alp) - ord('a') - shift) % 26 + ord('a'))
        elif 'A' <= alp <= 'Z':
            result += chr((ord(alp) - ord('A') - shift) % 26 + ord('A'))
        else:
            result += alp
    return result

def encode():
    text = input_text1.get(1.0,tk.END)
    result_text.delete(1.0, tk.END)
    result_text.insert(tk.END, caesar_encode(text, 3))

def decode():
    text = input_text1.get(1.0, tk.END)
    result_text.delete(1.0, tk.END)
    result_text.insert(tk.END, caesar_decode(text, 3))


window = tk.Tk()
window.title("Caesar Cipher")
window.geometry("500x200")


encoded_btn = tk.Button(window, text ="Encode", fg="green", command = encode)
encoded_btn.grid(row=1, column=0, padx = 20)

decoded_btn = tk.Button(window, text = "Decode", fg="green" ,command = decode)
decoded_btn.grid(row=1, column=1)

input_text1 = tk.Text(window, width = 40, height = 3)
input_text1.grid(row=0, column=2, padx=20)


result_text = tk. Text(window, width = 40, height =6)
result_text.grid(row=2, column=2, padx=20)

tk.mainloop()

