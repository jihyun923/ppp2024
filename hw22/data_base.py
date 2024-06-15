import os
import pickle

DB_FILE = "./calorie_db.pkl"


def read_db():
    if not os.path.exists(DB_FILE):
        return {}

    try:
        with open(DB_FILE, "rb") as f:
            data = pickle.load(f)
            return data
    except (EOFError, pickle.UnpicklingError):
        return {}



def write_db(food_db):
    with open(DB_FILE, "wb") as fout:
        pickle.dump(food_db, fout)


def main():
    kcal_total = read_db()
    print(f"현재까지 섭취한 음식 목록은 {kcal_total}입니다.")
    print(f"총 섭취한 칼로리는 {sum(kcal_total.values())}입니다.")

    while True:
        try:
            kcal = float(input("추가로 먹은 음식의 칼로리를 입력하세요: "))
        except ValueError:
            print("잘못된 입력입니다. 숫자를 입력하세요.")
            continue

        if kcal < 0:
            break
        food = input("음식 이름을 입력하세요: ")
        kcal_total[food] = kcal

    print(f"현재까지 섭취한 음식 목록은 {kcal_total}입니다.")
    print(f"총 섭취한 칼로리는 {sum(kcal_total.values())}입니다.")

    write_db(kcal_total)


if __name__ == '__main__':
    main()