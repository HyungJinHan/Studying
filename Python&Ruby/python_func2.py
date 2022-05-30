#!python
print("Content-type: text/html; charset=utf-8\n")
# ↑ Python을 연동시켜서 화면에 도출될 수 있게 하는 코드 ↑ (1~2)

def a(num):
# ()안에 num은 변수로써 적용
# 함수 호출 시, 숫자가 올 경우 그 숫자를 출력
    print(num)
    return "a"
a(10) # 결과 : 10

def A(num):
    return "A"*num
print(A(10)) # 결과 : AAAAAAAAAA (10*A)

def multiple(str, num):
# ()안에 첫번째 자리는 문자열, 두번째 자리는 숫자
    return str*num
print(multiple("AB", 2)) # 결과 : ABAB
