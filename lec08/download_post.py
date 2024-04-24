import requests
#import는 다른 사람이 짜놓은 코드를 사용하는 것
#폴더 밑으로 갈 땐 이름 작성 위로 갈 땐 ::? or ..을 쓰면 된대

URL = "https://coopjbnu.kr/function/ajax.get.rest.data.php"

data = { "code":"mobile1" }
#.은 현재 파일이라는 것을 의미
#한글이 깨지지 않게 하기 위해서 encoding 씀
#한글이 아니라면 default해도 됨
with open("./cafeteria_menu.html", "w", encoding="UTF-8") as f:
        res = requests.post(URL, data=data)
        res.encoding = "UTF-8"
        f.write(res.text)
#post 방식은 주소를 복붙해도 안 뜸 로그인이나 페이지를 들어갈 때 옵션을 안 줬기 때문