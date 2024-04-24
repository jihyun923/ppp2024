import requests
#import는 다른 사람이 짜놓은 코드를 사용하는 것
#폴더 밑으로 갈 땐 이름 작성 위로 갈 땐 ::? or ..을 쓰면 된대

URL = "https://coopjbnu.kr/menu/week_menu.php"

with open("./cafeteria_menu_weekly.html", "w", encoding="UTF-8") as f:
    res = requests.get(URL)
    res.encoding = "UTF-8"
    f.write(res.text)
#on3 -m pip install requests
#get방식은 주소를 그대로 카피해서 브라우저에 붙이면 그대로 사이트가 뜸