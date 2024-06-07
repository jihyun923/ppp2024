import telegram
from telegram.ext import Updater
from telegram.ext import MessageHandler, Filters
import random

def recommend_menu(choice):
    chinese_food = ["짜장면", "짬뽕", "마라탕", "양꼬치", "마파두부", "깐풍기",
                    "꿔바로우","깐쇼새우", "유린기", "고추잡채", "양장피", "마라샹궈"]
    korean_food = ["돌솥밥", "제육덮밥", "김밥", "국밥", "비빔밥", "삼계탕",
                   "감자탕", "냉면", "갈비탕", "오징어볶음", "아구찜", "동태찌개",
                   "닭갈비", "된장찌개", "삼겹살", "칼국수"]
    japanese_food = ["초밥", "회", "라멘", "돈카츠", "우동", "덴푸라", "오코노미야키",
                     "규동", "야키소바", "가츠동", "미소시루", "야키토리", "나베모노",
                     "가라아게", "스키야키", "오뎅", "소바", "나가사키 짬뽕"]
    western_food = ["스테이크", "파스타", "피자", "햄버거", "샐러드", "리조또",
                    "라자냐", "크림 스프", "크로켓", "프렌치 토스트", "바베큐 립",
                    "포크 립", "치킨 알프레도", "에그 베네딕트", "치킨 파마산"]
    if choice == "중식":
        selected_food = random.choice(chinese_food)
        return f"오늘은 {selected_food}(이)가 좋겠어요!"
    elif choice == "한식":
        selected_food = random.choice(korean_food)
        return f"오늘은 {selected_food}(이)가 좋겠어요!"
    elif choice == "일식":
        selected_food = random.choice(japanese_food)
        return f"오늘은 {selected_food}(이)가 좋겠어요!"
    elif choice == "양식":
        selected_food = random.choice(western_food)
        return f"오늘은 {selected_food}(이)가 좋겠어요!"
    else:
        return "알 수 없는 선택입니다. 중식, 한식, 일식, 양식 중에서 선택해 주세요."



def restaurant_menu(choice):
    chinese_restaurant = ["귀신반점", "오코오코", "백리향", "만리장성", "짬뽕지존", "천일반점", "구구양꼬치",
                          "용차이", "짬뽕관"]
    korean_restaurant = ["오일내", "계도리", "통집", "태평집", "헤이루", "덕천식당", "금암피순대", "완삼",
                         "마포갈매기", "고수닭갈비", "벼락", "연다라순대", "황제보쌈", "오늘김해뒷고기",
                         "동창야채닭갈비", "새빨간 죤스찜닭", "이문형 감자탕", "육쌈냉면", "닭터닭갈비", "일품양평해장국"]
    japanese_restaurant = ["코츠모", "멘야케이", "치히로", "면식당", "치쿠린", "돈가스집", "The담다", "오타마"
                            "야미", "백소정", "고씨네", "우리유부", "하루샤브", "츠케", "역전우동", "먹짜", "두부키친"
                           "산쪼메", "킨토토", "우마이"]
    western_restaurant = ["꽁꼬르드", "900달러피자", "고피자", "카페트럼펫", "TEAM레스토랑", "언더그라운드", "하우스37",
                          "롤링파스타", "코지버거", "벤티버거", "맘스터치", "써브웨이", "50end pizza", "파파존스", "맥도날드",
                          "유스샌드위치", "버거피아", "롯데리아", "버거킹", "와우케밥 치킨", "프랭크버거", "피자닭터", "피자마루",
                          "필라델피아"]

    if choice == "중식당":
        selected_food = random.choice(chinese_restaurant)
        return f"오늘은 {selected_food}에 가보는 게 좋겠어요!"
    elif choice == "한식당":
        selected_food = random.choice(korean_restaurant)
        return f"오늘은 {selected_food}에 가보는 게 좋겠어요!"
    elif choice == "일식당":
        selected_food = random.choice(japanese_restaurant)
        return f"오늘은 {selected_food}에 가보는 게 좋겠어요!"
    elif choice == "양식당":
        selected_food = random.choice(western_restaurant)
        return f"오늘은 {selected_food}에 가보는 게 좋겠어요!"
    else:
        return"알 수 없는 선택입니다. 중식당, 한식당, 일식당, 양식당 중에서 선택해 주세요."


token = '7293058712:AAHKiRmkRYP3owG1dssHnifd0o_6F9ufLJo'
chat_id = "7022511121"

bot = telegram.Bot(token)
bot.sendMessage(chat_id=chat_id, text="안녕하세요!")

updater = Updater(token=token, use_context=True)
dispatcher = updater.dispatcher
updater.start_polling()

def handler(update, context):
    user_text = update.message.text
    if user_text == "안녕":
        bot.send_message(chat_id=id, text="안녕하세요!")
    elif user_text in ["점심","저녁","메뉴 추천", "매뉴 추천", "매뉴추천", "메뉴추천"]:
        bot.send_message(chat_id=update.message.chat_id, text="중식, 한식, 일식, 양식 중 무엇을 먹고 싶으신가요? 한 가지만 골라 주세요.")
    elif user_text in ["중식", "한식", "일식", "양식"]:
        menu = recommend_menu(user_text)
        bot.send_message(chat_id=update.message.chat_id, text=menu)
    elif user_text in ["고마워", "고마워!"]:
        bot.send_message(chat_id=update.message.chat_id, text="별 말씀을요!")
    elif user_text in ["다른 메뉴 추천", "다른메뉴 추천", "다른메뉴추천", "다른 메뉴추천", "다른 메뉴 추천해 줘"]:
        menu = recommend_menu(user_text)
        bot.send_message(chat_id=update.message.chat_id, text=menu)
    elif user_text in ["식당 추천","식당추천", "식당 추천해 줘", "식당 추천해줘", "식당 추천 부탁해"]:
        bot.send_message(chat_id=update.message.chat_id, text="중식당, 한식당, 일식당, 양식당 중 무엇을 먹고 싶으신가요? 한 가지만 골라 주세요.")
    elif user_text in ["중식당", "한식당", "일식당", "양식당"]:
        res = restaurant_menu(user_text)
        bot.send_message(chat_id=update.message.chat_id, text=res)
    else:
        bot.send_message(chat_id=update.message.chat_id, text="이해를 못했습니다.")

echo_handler = MessageHandler(Filters.text, handler)
dispatcher.add_handler(echo_handler)
