#!python
print("Content-type: text/html; charset=utf-8\n")
# ↑ Python을 연동시켜서 화면에 도출될 수 있게 하는 코드 ↑ (1~2)

import sys
# sys 사용을 위함

input_name = input("아이디를 입력해주세요.\n")
fam = ["hsh", "jhs", "hhj1", "hhj2"]

for member in fam:
# fam 내부의 member에 대한 반복문
    if member == input_name:
    # fam 내부의 member와 input_name의 입력값이 같으면
        print("Hello!, "+member)
        # hhj1 입력 결과 : Hello!, hhj1
        sys.exit()
        # if문이 끝나면 종료시키는 코드

print("GET OUT!")
# abc라는 값이 fam의 member와 다를 경우 출력
