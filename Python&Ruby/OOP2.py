#!python
print("Content-type: text/html; charset=utf-8\n")
# ↑ Python을 연동시켜서 화면에 도출될 수 있게 하는 코드 ↑ (1~2)

class C:
    def __init__(self, n1):
    # 생성자
        self.value = n1
    def show(self):
        print(self.value)

c1 = C(10)
# c1은 인스턴스를 의미, (10)은 위의 self.value 값
print(c1.value) # 결과 : 10

c1.value = 100
print(c1.value) # 결과 : 100
# 외부의 메소드를 통해서 인스턴스의 변수에 접근 가능

c1.value = 1000
c1.show() # 결과 : 1000
# 인스턴스에 소속된 메소드를 외부에서 사용하는 형식도 사용 가능
