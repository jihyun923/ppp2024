import random

def gugudan():
    random_num = random.randint(1,9)
    random_num2 = random.randint(1,9)
    answer = random_num * random_num2
    quiz = int(input(f"답을 입력하세요. {random_num} * {random_num2} = "))

    return quiz, answer


def main():
    score = 0
    total_quiz = 0

    while True:
        quiz, answer = gugudan()
        total_quiz += 1

        if quiz == answer:
            print("정답입니다.")
            score += 1
        else:
            print(f"틀렸습니다. 정답은 {answer}입니다.")

        continue_game = input(f"총 {score}점입니다. 계속 하시겠습니까? (y/n):")

        if continue_game.lower() == 'y':
            continue
        elif continue_game.lower() == 'n':
            print(f"수고하셨습니다. 총 {total_quiz}문제 중 {score}개 맞히셨습니다.")
            break
        else:
            print("y 또는 n을 입력해 주세요.")

        print(f"최종 점수: {score}점 / 총 제출된 문제 수: {total_quiz}")


if __name__=="__main__":
    main()
