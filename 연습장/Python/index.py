#!python
print("Content-type: text/html; charset=utf-8\n")
# ↑ Python을 연동시켜서 화면에 도출될 수 있게 하는 코드 ↑ (1~2)

import cgi, os, View, html_sanitizer
sanitizer = html_sanitizer.Sanitizer()
# View라는 폴더를 가져오기 위해 View를 모듈로 입력 / 보안을 위해 html_sanitizer 모듈을 입력
# os라는 모듈로 묶여서 실행되는 명령어를 실행시킬 수 있음
# import가 안된다면 설치경로를 정확히 보자

form = cgi.FieldStorage()
if "id" in form: #form안에 id 값이 있는 경우 else에 해당하는 값을 도출
    title = pageId = form["id"].value
    description = open("Data/"+pageId, "r").read()
    # description = description.replace("<script>", "")
    # description = description.replace("</script>", "")
    # 내용에 해당하는 문자에서 script 태그를 공백으로 바꾸도록 지정
    title = sanitizer.sanitize(title)
    # title 내의 원치 않는 태그를 거를 수 있도록 지정
    description = sanitizer.sanitize(description)
    # description 내의 원치 않는 태그를 거를 수 있도록 지정
    # ()안의 내용을 sanitaze를 실시하여 위험한 태그를 지우거나 html 태그로 변환
    update_link = '<a href="update.py?id={}">update</a>'.format(pageId)
    # pageId에 따라 update 버튼을 생성
    delete_action = '''
        <form action="process_delete.py" method="post">
            <input type="hidden" name="pageId" value="{}">
            <input type="submit" value="delete">
        </form>
    '''.format(title)

else:
    title = pageId = "Welcome"
    description = "Hello, Web"
    update_link = ""
    delete_action = ""
    # pageId 값이 없는 경우 공백으로 지정해서 update 버튼 없애기

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
  {update_link}
  {delete_action}
  <h2>{title}</h2>
  <p>{desc}</p>
</body>
</html>
'''.format(title=title, desc=description, listStr=View.getList(), update_link=update_link, delete_action=delete_action))
# View라는 모듈을 불러오기 위해서 View.getList() 입력
