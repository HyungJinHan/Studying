#!python
print("Content-type: text/html; charset=utf-8\n")
# ↑ Python을 연동시켜서 화면에 도출될 수 있게 하는 코드 ↑ (1~2)

class Class1(object):
    def method1(self):
        return "m1"

class Class2(Class1):
# 상속받을 class를 ()에 지정
    def method2(self):
        return "m2"

class Class3(Class2):
# 상속받을 class를 ()에 지정
    def method3(self):
        return "m3"

c1 = Class1()
print(c1.method1()) # 결과 : m1

c2 = Class2()
print(c2.method1()) # 결과 : m1 (Class1에게 상속받음)
print(c2.method2()) # 결과 : m2

c3 = Class3()
print(c3.method1()) # 결과 : m1 (Class1에게 상속받음)
print(c3.method2()) # 결과 : m2 (Class2에게 상속받음)
print(c3.method3()) # 결과 : m3

# 상속을 통해서 인스턴스 내에 없는 메소드 출력 가능
# Class1의 메소드의 값이 변경되면 Class2, Class3의 내용도 바뀜
