#!python
print("Content-type: text/html; charset=utf-8\n")
# ↑ Python을 연동시켜서 화면에 도출될 수 있게 하는 코드 ↑ (1~2)

import math
# math라는 모듈을 사용하기 위해 불러오는 역할

print(math.ceil(2.2)) # 3 (소수점 올림)
print(math.floor(2.9)) # 2 (소수점 내림)
print(math.sqrt(121)) # 11.0 (제곱근 반환)
print(math.pi) # 3.141592653589793 (원주율)
print(math.pow(2, 15)) # 32768.0 (2의 15제곱)
