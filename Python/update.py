#!python
print("Content-type: text/html; charset=utf-8\n")
# ↑ Python을 연동시켜서 화면에 도출될 수 있게 하는 코드 ↑ (1~2)

import cgi, os, View #os라는 모듈로 묶여서 실행되는 명령어를 실행시킬 수 있음

form = cgi.FieldStorage()
if "id" in form: #form안에 id 값이 있는 경우 else에 해당하는 값을 도출
    pageId = form["id"].value
    description = open("Data/"+pageId, "r").read()
else:
    pageId = "Welcome"
    description = "Hello, Web"

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
  <form action="process_update.py" method="post">
  <!-- 전송할 파일을 action 태그로 지정, method를 post로 지정해서 함부로 수정할 수 없도록 하기 -->
      <input type="hidden" name="pageId" value="{form_default_title}"></p>
      <!--제목이 아닌 pageId 값의 수정을 막기 위해 pageId 수정 칸을 따로 만들고 숨기기 -->
      <p><input type="text" name="Title" placeholder="Title" value="{form_default_title}"></p>
      <!-- 제목 생성을 위한 input 태그 / 수정 시에 텍스트 박스에 원래 글이 남아있도록 value 값을 지정 -->
      <p><textarea rows="5" name="Description" placeholder="Description">{form_default_desc}</textarea></p>
      <!-- 여러줄의 내용 입력을 위한 textbox / 수정 시에 텍스트 박스에 원래 글이 남아있도록 태그 사이에 값 지정 -->
      <p><input type="submit"></p> <!--  제출 버튼 -->
  </form> <!-- 제목과 내용을 제출하기 위해 form으로 감싸기 -->
</body>
</html>
'''.format(title=pageId, desc=description, listStr=View.getList(), form_default_title=pageId, form_default_desc=description))
# 수정사항의 경우 form_default_title에는 pageId, form_default_desc에는 description을 지정

# ?id=xxx -> 쿼리스트링
