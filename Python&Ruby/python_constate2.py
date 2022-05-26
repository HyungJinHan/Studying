#!python
print("Content-type: text/html; charset=utf-8\n")
# ↑ Python을 연동시켜서 화면에 도출될 수 있게 하는 코드 ↑ (1~2)

PW_1 = "1210"
PW_2 = "7304"
in_str = input("아이디를 입력해주세요.\n")
# input을 통해 입력값 확인

if PW_1 == in_str:
# PW_1 == in_str : Hello Master
# PW_1과 in_str의 datatype이 숫자와 문자열로
# 다르기 때문에 숫자를 문자열로 바꿔야 true값 출력
  print("Hello Master")
elif PW_2 == in_str:
# PW_2 == in_str : Hello User (elif 주의)
  print("Hello User")
else:
# PW_1, PW_2 != in_str : GET OUT!
  print("GET OUT!")
