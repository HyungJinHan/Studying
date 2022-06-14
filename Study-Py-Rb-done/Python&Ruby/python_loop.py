#!python
print("Content-type: text/html; charset=utf-8\n")
# ↑ Python을 연동시켜서 화면에 도출될 수 있게 하는 코드 ↑ (1~2)

i = 0
while i < 10:
    print("Hello Python "+str(i*9)+"")
    # Hello Python은 문자열, i는 숫자이기 때문에
    # 합쳐서 출력이 불가능
    # i를 문자화 시켜서 합쳐서 출력해야 함
    # str(i) : 숫자인 i를 문자화 시킴
    # i에 9를 곱하도록 지정 str(i*9)
    # Hello Python에 "+str(i*9)+" 추가
    # +xxx+ : 문자열 + xxx + 문자열 의미
    i = i + 1
# 결과
# Hello Python 0
# Hello Python 9
# Hello Python 18
# Hello Python 27
# Hello Python 36
# Hello Python 45
# Hello Python 54
# Hello Python 63
# Hello Python 72
# Hello Python 81
