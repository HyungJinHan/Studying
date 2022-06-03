#!python
print("Content-type: text/html; charset=utf-8\n")
# ↑ Python을 연동시켜서 화면에 도출될 수 있게 하는 코드 ↑ (1~2)

import lib
# lib이라는 개별적인 파일로써의 module 불러오기

obj = lib.A()
# lib의 코드를 불러오기 위해 lib.A() 사용
print(obj.a()) # 결과 : a

# lib.py 내용
# class A:
#     def a(self):
#         return "a"
