#!python
print("Content-type: text/html; charset=utf-8\n")
# ↑ Python을 연동시켜서 화면에 도출될 수 있게 하는 코드 ↑ (1~2)

class C:
    def __init__(self, n1):
    # 생성자
        self.__value = n1
    def show(self):
        print(self.__value)

c1 = C(10)
# c1은 인스턴스를 의미, (10)은 위의 self.value 값
# print(c1.__value) # 결과 : Error
# 외부에서 인스턴스 변수에 접근할 수 없도록 __ 사용

c1.show() # 결과 : 10
# 인스턴스의 내부 메소드를 사용하기 때문에 사용 가능
