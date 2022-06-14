#!python
print("Content-type: text/html; charset=utf-8\n")
# ↑ Python을 연동시켜서 화면에 도출될 수 있게 하는 코드 ↑ (1~2)

ID_1 = "hhj"
PW_1 = "1210"
input_ID = input("아이디를 입력해주세요.\n")
input_PW = input("비밀번호를 입력해주세요.\n")

if ID_1 == input_ID and PW_1 == input_PW:
    print("Welcome Master!")
    # ID와 PW가 맞은 경우
else:
  print("잘못된 아이디 또는 비밀번호입니다.")
  # ID와 PW가 틀린 경우
