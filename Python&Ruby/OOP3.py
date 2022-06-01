#!python
print("Content-type: text/html; charset=utf-8\n")
# ↑ Python을 연동시켜서 화면에 도출될 수 있게 하는 코드 ↑ (1~2)

class C:
    def __init__(self, n1):
    # 생성자
        self.value = n1
    def show(self):
        print(self.value)
    def getValue(self):
        return self.value
    def setValue(self, n1):
    # value값 지정을 위해 ()에 n1 입력
        self.value = n1

c1 = C(10)
# c1은 인스턴스를 의미, (10)은 위의 self.value 값
print(c1.getValue()) # 결과 : 10
# return self.value으로 인해 C(10)으로 정한 값인 10 출력

c1.setValue(100)
print(c1.getValue()) # 결과 : 100
# c1.setValue(100)을 통해 100을 value값으로 지정 후 출력
