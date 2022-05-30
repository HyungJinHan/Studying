#!python
print("Content-type: text/html; charset=utf-8\n")
# ↑ Python을 연동시켜서 화면에 도출될 수 있게 하는 코드 ↑ (1~2)

import import_ex1, import_ex2
# import_ex1.py, import_ex2.py의 함수를 불러옴

from import_ex1 import aaa
# import_ex1.py 내의 aaa에 해당하는 함수만을 불러옴

from import_ex2 import aa
# import_ex2.py 내의 aa에 해당하는 함수만을 불러옴

def a():
    return "A"
print(a()) # 결과 : A

print(import_ex1.a()) # 결과 : B
# import를 통해 import_ex.py에 있는 함수를 불러옴

print(import_ex2.a()) # 결과 : C

print(aaa()) # 결과 : BBB (import_ex1.py)
# from import_ex1 import aaa를 통해 aaa라는 함수만을 불러왔기 때문

print(aa()) # 결과 : CC (import_ex2.py)
# from import_ex2 import aa를 통해 aa라는 함수만을 불러왔기 때문

# === import_ex1.py 내용 ===
# def a():
#     return "B"

# def aa():
#     return "BB"

# def aaa():
#     return "BBB"

# === import_ex2.py 내용 ===
# def a():
#     return "C"

# def aa():
#     return "CC"

# def aaa():
#     return "CCC"
