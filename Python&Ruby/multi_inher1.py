#!python
print("Content-type: text/html; charset=utf-8\n")
# ↑ Python을 연동시켜서 화면에 도출될 수 있게 하는 코드 ↑ (1~2)

class C1():
    def c1_m(self):
        return "Parent(C1)"

class C2():
    def c2_m(self):
        return "Child(C2)"

class C3():
    def c3_m(self):
        return "Child(C3)"

class C4(C1, C2, C3):
# 다중상속의 경우 상속을 받고 있는 객체에는 작동 X
# ex : C2(C1) / C3(C1, C2) → Error
    pass

c1 = C1()
print(c1.c1_m()) # 결과 : Parent(C1)

c2 = C2()
print(c2.c2_m()) # 결과 : Child(C2)

c3 = C3()
print(c3.c3_m()) # 결과 : Child(C3)

c4 = C4()
print(c4.c1_m()) # 결과 : Parent(C1)
print(c4.c2_m()) # 결과 : Child(C2)
print(c4.c3_m()) # 결과 : Child(C3)
