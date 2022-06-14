#!python
print("Content-type: text/html; charset=utf-8\n")
# ↑ Python을 연동시켜서 화면에 도출될 수 있게 하는 코드 ↑ (1~2)

import sys, module_login as log
# sys 사용을 위함
# 모듈인 module_login를 불러오고 log로 지정

input_id = input("아이디를 입력해주세요.\n")

if log.login(input_id):
# 모듈을 불러왔기 때문에 지정한 명칭인 log.xxx로 수정
    print("Hello! "+input_id)
    # hhj1 입력 결과 : Hello! hhj1
else:
    print("GET OUT!")

# === module_login.py의 내용 ===

# def login(id):
#     fam = ["hsh", "jhs", "hhj1", "hhj2"]
#     for member in fam:
#         if member == id:
#             return True
#     return False
