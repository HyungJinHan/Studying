#!python
print("Content-type: text/html; charset=utf-8\n")
# ↑ Python을 연동시켜서 화면에 도출될 수 있게 하는 코드 ↑ (1~2)

import cgi
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
    <li><a href="index.py?id=HTML">HTML</a></li>
    <li><a href="index.py?id=CSS">CSS</a></li>
    <li><a href="index.py?id=JavaScript">JavaScript</a></li>
    <li><a href="index.py?id=Python">Python</a></li>
  </ol>
  <h2>{title}</h2>
  <p>{desc}</p>
</body>
</html>
'''.format(title=pageId, desc=description))
