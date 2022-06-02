#!python
print("Content-type: text/html; charset=utf-8\n")
# ↑ Python을 연동시켜서 화면에 도출될 수 있게 하는 코드 ↑ (1~2)

class C1:
    def m(self):
        return "Parent"

class C2(C1):
    pass
    # 해당 class에 내용이 없더라도 실행시키도록 함

class C3(C2):
    def m(self):
        return "Child"

class C4(C3):
    def m(self):
        return super().m() + " HHJ"
        # 부모 class 사용을 위한 메소드

o = C2()
print(o.m())
 # 결과 : Parent (C1에게 상속받음)

o1 = C3()
print(o1.m())
# 결과 : Child (C2에게 상속받았지만 Override함)

o2 = C4()
print(o2.m())
# 결과 : Child HHJ (super().m()을 통해 C3의 값 출력)

# Python의 super().m()
# super() : 부모 객체를 의미 (부모 객체가 무엇인지를 찾는 역할)
# m() : 부모 객체의 메소드 값을 의미 (부모 객체의 메소드 값을 출력하기 위한 역할)

# 결론 : Python에서의 super()는 부모 객체를 의미
