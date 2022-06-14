#!python
print("Content-type: text/html; charset=utf-8\n")
# ↑ Python을 연동시켜서 화면에 도출될 수 있게 하는 코드 ↑ (1~2)

class Cal(object):
    def __init__(self, n1, n2):
    # 생성자, constructor
        if isinstance(n1, int):
            self.n1 = n1
        if isinstance(n2, int):
            self.n2 = n2
    def add(self): # 메소드
        return self.n1 + self.n2
    def subtract(self): # 메소드
        return self.n1 - self.n2
    def setN1(self, n):
        if isinstance(n, int):
        # 첫번째 인자가 두번째 인자의 인스턴스인지 체크하는 조건문
            self.n1 = n
    def getN1(self):
        return self.n1

class CalMultiply(Cal):
    def multiply(self):
        return self.n1 * self.n2

class CalDivide(CalMultiply):
    def divide(self):
        return self.n1 / self.n2

c1 = CalMultiply(100, 10) # 생성자도 상속받음
print(c1.multiply()) # 결과 : 1000
print(c1.add()) # 결과 : 110 (Cal에게 상속받음)
print(c1.subtract()) # 결과 : 90 (Cal에게 상속받음)

c2 = CalDivide(200, 10)
print(c2.multiply()) # 결과 : 2000 (CalMultiply에게 상속받음)
print(c2.divide()) # 결과 : 20.0

c1.setN1(500)
print(c1.getN1()) # 결과 500
print(c2.getN1()) # 결과 : 200
print(c1.multiply()) # 결과 : 5000
