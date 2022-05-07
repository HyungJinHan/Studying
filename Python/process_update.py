#!python

import cgi, os
form = cgi.FieldStorage()
pageId = form["pageId"].value # pageId는 별도로 받아서 ?id=값이 바뀌지 않도록 지정
Title = form["Title"].value
Description = form["Description"].value
# 개발자 도구를 통해 전송된 데이터를 form 전송 값으로 지정

opened_file = open("Data/"+pageId, "w") # Title은 바뀔 수 있기 때문에 pageId로 변경
# 쓰기 전용 (w) Title이라는 파일을 Data 폴더에 만들기
opened_file.write(Description) # Description의 내용에 해당하는 값이 입력되도록 지정
opened_file.close() # 윈도우의 경우 close를 기입해서 오류가 나지 않도록 해야함

os.rename("Data/"+pageId, "Data/"+Title)
# os.rename(현재 파일의 이름(scr), 바꿔야 할 이름(dst))

#Redirection (밑의 내용 외의 print 값이 존재할 시, 헤더 오류 발생으로 모든 print는 제거)
print("Location: index.py?id="+Title) # Title을 추가한 쿼리스트링 주소로 이동하도록 지정
print() # 이게 있어야 python 오류가 안남, 이유 모름
