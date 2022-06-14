#!python
print("Content-type: text/html; charset=utf-8\n")
# ↑ Python을 연동시켜서 화면에 도출될 수 있게 하는 코드 ↑ (1~2)

class Cs:
    @staticmethod
    # 장식자 : static 소속의 메소드임을 표시하는 규칙
    def static_method():
        print("Static Method")
    @classmethod
    # 장식자 : class 소속의 메소드임을 표시하는 규칙
    def class_method(cls):
    # class 소속의 메소드의 경우 ()에 cls 입력
        print("Class Method")
    def instance_method(self):
    # 인스턴스 소속의 메소드의 경우 ()에 self 입력
        print("Instance Method")

Cs.static_method() # 결과 : Static Method
Cs.class_method() # 결과 : Class Method

i = Cs()
# 인스턴스 생성
i.instance_method() # 결과 : Instance Method

i.static_method() # 결과 : Error
i.class_method() # 결과 : Error
Cs.instance_method() # 결과 : Error
