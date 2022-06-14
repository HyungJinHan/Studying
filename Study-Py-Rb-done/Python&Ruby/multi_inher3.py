#!python
print("Content-type: text/html; charset=utf-8\n")
# ↑ Python을 연동시켜서 화면에 도출될 수 있게 하는 코드 ↑ (1~2)

class CalMultiply():
    def multiply(self):
        return self.n1 * self.n2

class CalDivide():
    def divide(self):
        return self.n1 / self.n2

class Cal(CalMultiply, CalDivide):
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
    def setN2(self, n):
        if isinstance(n, int):
        # 첫번째 인자가 두번째 인자의 인스턴스인지 체크하는 조건문
            self.n2 = n
    def getN1(self):
        return self.n1
    def getN2(self):
        return self.n2

c = Cal(100, 10)
print(c.add()) # 결과 : 110
print(c.subtract()) # 결과 : 90
print(c.multiply()) # 결과 : 1000 (CalMultiply에게 상속받음)
print(c.divide()) # 결과 : 10.0 (CalDivide에게 상속받음)

c.setN1(500)
c.setN2(100)
print("n1 =",c.getN1(),",","n2 =",c.getN2()) # 결과 : n1 =  500 , n2 = 100
print(c.getN2()) # 결과 : 100
print(c.multiply()) # 결과 : 50000 (CalMultiply에게 상속받음)
print(c.divide()) # 결과 : 5.0 (CalDivide에게 상속받음)
