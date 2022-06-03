#!python
print("Content-type: text/html; charset=utf-8\n")
# ↑ Python을 연동시켜서 화면에 도출될 수 있게 하는 코드 ↑ (1~2)

class C1():
    def c1_m(self):
        return "Parent(C1)"
    def c1_1_m(self):
        return "Parent(C1_1)"

class C2():
    def c2_m(self):
        return "Child(C2)"
    def c1_m(self):
        return "Parent(C2)"
        # 기대값 : print(c4.c1_m()) = Parent(C2)

class C3():
    def c3_m(self):
        return "Child(C3)"
    def c1_1_m(self):
        return super().c1_1_m() + " C3"
        # 기대값 : print(c4.c1_1_m()) = Parent(C1_1) C3

class C4(C1, C2, C3):
# 다중상속의 경우 상속을 받고 있는 객체에는 작동 X
# ex : C2(C1) / C3(C1, C2) → Error
    pass

c4 = C4()
print(c4.c1_m()) # 결과 : Parent(C1) / Parent(C2) X
print(c4.c2_m()) # 결과 : Child(C2)
print(c4.c3_m()) # 결과 : Child(C3)
print(c4.c1_1_m()) # 결과 : Parent(C1_1) / Parent(C1_1) C3 X

# 다중 상속의 문제점은 override의 개념으로 접근하는 것이 아닌
# 값의 부모 객체를 class C4(C1, C2, C3)의 인자 순서에 따라 찾는 개념으로 접근
