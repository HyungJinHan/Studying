#!python
print("Content-type: text/html; charset=utf-8\n")
# ↑ Python을 연동시켜서 화면에 도출될 수 있게 하는 코드 ↑ (1~2)

print("aaa") # 결과 : aaa
# print도 일종의 함수

len_ex = len("aaa")
print(len_ex) # 결과 : 3 (문자수)

# 내장함수 : python 자체에 기본적으로 내장된 함수

def ex_1(): # ex_1을 함수로 정의
    print("aaa")
    # def ex_1 밑으로의 내용은 ex_1이라는 함수의 본문
    len_ex1 = len("Hallo Function")
    print(len_ex1)
    i = 0
    while i < 2:
        print("Hello Function "+str(i)+"")
        i = i + 1

ex_1()
# 정의된 함수를 호출
# 결과
# aaa
# 14
# Hello Function 0
# Hello Function 1
