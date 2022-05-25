#!python
print("Content-type: text/html; charset=utf-8\n")
# ↑ Python을 연동시켜서 화면에 도출될 수 있게 하는 코드 ↑ (1~2)

import math
# math를 사용하기 위해 import를 해야함

print(100+100); # 200
print(100-100); # 0
print(100*100); # 10000
print(100/100); # 1.0

print(math.ceil(2.2)) # 3 (소수점 올림)
print(math.floor(2.6)) # 2 (소수점 내림)
print(math.trunc(2.8)) # 2 (소수점 버림)
print(math.pow(2, 10)) # 1024.0 (2의 10제곱)
print(math.pi) # 3.141592653589793 (소문자로 pi)
