#!python

import cgi, os
form = cgi.FieldStorage()
pageId = form["pageId"].value
# 개발자 도구를 통해 전송된 데이터를 form 전송 값으로 지정

os.remove("Data/"+pageId)

#Redirection (밑의 내용 외의 print 값이 존재할 시, 헤더 오류 발생으로 모든 print는 제거)
print("Location: index.py") # 삭제 후 메인 화면으로 넘어갈 수 있도록 지정
print() # 이게 있어야 python 오류가 안남, 이유 모름
