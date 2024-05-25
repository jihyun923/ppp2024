import time
import winsound

def sos():
    for i in range(0, 3):
        winsound.Beep(2000, 100)

def main():
    count = int(input("시간(초)을 입력하세요."))

    while True:
        print(f"카운트다운... {count}")
        time.sleep(1)
        count -= 1

        if count <= 0:
            break
    print("Bomb!")
    sos()

if __name__ == '__main__':
    main()