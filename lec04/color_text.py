def colored(r, g, b, text):
    return "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(r, g, b,
text)
def hello(name):
    print(f"{colored(0,255,0, name)}님 안녕하세요.")
    
print(colored(255, 255, 0, 'hello world'))
hello("홍길동")