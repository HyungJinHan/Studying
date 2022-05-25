#!python
print("Content-type: text/html; charset=utf-8\n")
# ↑ Python을 연동시켜서 화면에 도출될 수 있게 하는 코드 ↑ (1~2)

print(1==1) # True (정확히 동일)
print(1==2) # False (다름)
print(1=="one") # False (숫자와 문자로 동일하지 않음)
# == : 동등 비교 연산자

a=1
b=1
print(a==b) # True
# = : 대입 연산자

print(1>2) # False
print(1<2) # True

print(1<=1) # True (작거나 같음)
print(1!=3) # True (다름)

print(True) # 맨 앞글자 대문자
print(False) # 맨 앞글자 대문자
