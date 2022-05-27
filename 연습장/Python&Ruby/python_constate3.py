#!python
print("Content-type: text/html; charset=utf-8\n")
# ↑ Python을 연동시켜서 화면에 도출될 수 있게 하는 코드 ↑ (1~2)

PW_1 = "hhj"
PW_2 = "hsh"
in_str = input("아이디를 입력해주세요.\n")

if PW_1 == in_str or PW_2 == in_str:
# or을 통해 둘 중에 하나가 맞을 시 true
  print("Welcome!")
else:
  print("GET OUT!")
