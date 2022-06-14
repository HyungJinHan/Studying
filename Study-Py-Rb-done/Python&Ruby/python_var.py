#!python
print("Content-type: text/html; charset=utf-8\n")
# ↑ Python을 연동시켜서 화면에 도출될 수 있게 하는 코드 ↑ (1~2)

x = 100 # 변수 지정
y = 100
print(x+y) # 200

z = "Hello World"
print("z") # z
print(z) # Hello World
# 변수 지정 후 출력 시, ""제거

hi = "Hello "
print(hi+"World") # Hello World

name = "HHJ"
print("Hello World! I'm "+name+"!")
# Hello World! I'm HHJ!
print("Nice to meet you, "+name+"")
# Nice to meet you, HHJ

지원금 = 1000000
신청인 = 10
지원기업 = 20
print((지원금*신청인)/지원기업, "원") # 500000.0 원
