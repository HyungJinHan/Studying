import os, html_sanitizer

def getList(): # 목록을 불러온다는 의미의 함수 지정 / format에 listStr을 getList()로 지정
    sanitizer = html_sanitizer.Sanitizer()
    # 불러오는 목록도 sanitize로 설정
    files = os.listdir("Data") #files라는 함수로 묶어서 Data 폴더에 있는 파일을 불러온다
    # for data in files:
    #     listStr = listStr + data #비어있는 문자열 + Data 내의 파일
    # print(listStr) #공백 + CSS + HTML + JavaScript + Python
    listStr = "" #비어있는 문자열 임의로 생성
    for item in files:
        item = sanitizer.sanitize(item)
        # item을 불러올 때 sanitize로 걸러주며 불러옴
        listStr = listStr + '<li><a href="index.py?id={name}">{name}</a></li>'.format(name=item)
    #''작은 따옴표로 <li></li>를 묶어야 하나 봄
    # li 형식으로 item이라는 함수를 name으로 포맷팅을 한 후, 웹 주소도 id 값을 {name}으로 포맷팅,
    # li의 이름도 {name}으로 포맷팅해서 화면에 도출
    return listStr # 해당 값을 화면에 표현
