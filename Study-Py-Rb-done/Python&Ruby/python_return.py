#!python
print("Content-type: text/html; charset=utf-8\n")
# ↑ Python을 연동시켜서 화면에 도출될 수 있게 하는 코드 ↑ (1~2)

def a3():
    return "aaa"
print(a3()) # 결과 : aaa

def a2():
    a = "aa"
    return a
print(a2()) # 결과 : aa

def a1():
    print("before")
    return "a"
    print("after")
a1() # 결과 : before
print(a1())
 # 결과
 # before
 # a
 # (return은 함수를 종료하므로 after 출력 X)
