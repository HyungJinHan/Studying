#!python
print("Content-type: text/html; charset=utf-8\n")
# ↑ Python을 연동시켜서 화면에 도출될 수 있게 하는 코드 ↑ (1~2)

print("Hello World") # Hello World
print("Hello "+"World") # Hello World
print("Hello "*3) # Hello Hello Hello
# 문자열에는 빼기, 나누기는 없음

print("Hello World"[0]) # H - 1(0)번째 문자
print("Hello World"[1]) # e - 2(1)번째 문자
print("Hello World"[2]) # l - 3(2)번째 문자
print("Hello World"[3]) # l - 4(3)번째 문자

print("hello world".capitalize()) # Hello world
# 제일 앞글자 대문자화

print("hello world".upper()) # HELLO WORLD
# 전체를 대문자화

print("Hello World".__len__()) # 11 (_ 두번 주의)
print(len("Hello World")) # 11
# 해당 문자열의 문자 개수

print("hi World".replace("hi", "Hello")) # HELLO WORLD
# hi를 Hello로 치환

print("Hello\nWorld") # HELLO
                      # WORLD
# \n (new line) : 줄바꿈

print("Hello\tWorld") # Hello	World
# \t (tab) : 들여쓰기

print("\a") # 경고음 재생
# \a (alert)

# Datatype
print("100"+"100") # 100100 (문자로써의 100)
print(100+100) # 200 (숫자로써의 100)
