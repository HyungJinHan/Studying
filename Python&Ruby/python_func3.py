#!python
print("Content-type: text/html; charset=utf-8\n")
# ↑ Python을 연동시켜서 화면에 도출될 수 있게 하는 코드 ↑ (1~2)

import sys
# sys 사용을 위함

input_id = input("아이디를 입력해주세요.\n")

def login(id):
    fam = ["hsh", "jhs", "hhj1", "hhj2"]
    for member in fam:
        if member == id:
        # 함수를 정의할 때의 () 안의 id값과 같은지를 확인
            return True
            # return값을 true로 지정을 하면 밑의 if문에서 true의 값에 해당하는 값이 출력
    return False
    # return값을 false로 지정을 하면 밑의 if문에서 false의 값에 해당하는 값이 출력

if login(input_id):
    print("Hello! "+input_id)
    # hhj1 입력 결과 : Hello! hhj1
else:
    print("GET OUT!")
