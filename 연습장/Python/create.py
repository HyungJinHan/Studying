#!python
print("Content-type: text/html; charset=utf-8\n")
# ↑ Python을 연동시켜서 화면에 도출될 수 있게 하는 코드 ↑ (1~2)

import cgi, os #os라는 모듈로 묶여서 실행되는 명령어를 실행시킬 수 있음

form = cgi.FieldStorage()
if "id" in form: #form안에 id 값이 있는 경우 else에 해당하는 값을 도출
    pageId = form["id"].value
    description = open("Data/"+pageId, "r").read()
else:
    pageId = "Welcome"
    description = "Hello, Web"

files = os.listdir("Data") #files라는 함수로 묶어서 Data 폴더에 있는 파일을 불러온다

# for data in files:
#     listStr = listStr + data #비어있는 문자열 + Data 내의 파일
# print(listStr) #공백 + CSS + HTML + JavaScript + Python

listStr = "" #비어있는 문자열 임의로 생성

for item in files:
    listStr = listStr + '<li><a href="index.py?id={name}">{name}</a></li>'.format(name=item)
#''작은 따옴표로 <li></li>를 묶어야 하나 봄
# li 형식으로 item이라는 함수를 name으로 포맷팅을 한 후, 웹 주소도 id 값을 {name}으로 포맷팅,
# li의 이름도 {name}으로 포맷팅해서 화면에 도출

print('''<!doctype html>
<html>
<head>
  <title>WEB1 - Welcome</title>
  <meta charset="utf-8">
</head>
<body>
  <h1><a href="index.py">WEB</a></h1>
  <ol>
    {listStr} <!-- 위에서 만든 파일 불러오기 포맷팅을 이식 -->
  </ol>
  <a href="create.py">Create</a>
  <form action="process_create.py" method="post">
  <!-- 전송할 파일을 action 태그로 지정, method를 post로 지정해서 함부로 수정할 수 없도록 하기 -->
      <p><input type="text" name="Title" placeholder="Title"></p> <!-- 제목 생성을 위한 input 태그 -->
      <p><textarea rows="5" name="Description" placeholder="Description"></textarea></p> <!-- 여러줄의 내용 입력을 위한 textbox -->
      <p><input type="submit"></p> <!--  제출 버튼 -->
  </form> <!-- 제목과 내용을 제출하기 위해 form으로 감싸기 -->
</body>
</html>
'''.format(title=pageId, desc=description, listStr=listStr))

# ?id=xxx -> 쿼리스트링
