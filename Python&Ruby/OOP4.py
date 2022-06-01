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

c1 = Cal(100, 10)
print(c1.add()) # 더하기 / 결과 : 110
print(c1.subtract()) # 빼기 / 결과 : 90

c1.setN1("one")
c1.n2 = 30
print(c1.add()) # 결과 : 130 → 문자 1 + 숫자 30
print(c1.subtract())
# 위의 문자 1은 무시되고 c1 = Cal(100, 10)의
# 100과 c1.n2 = 30의 계산 값인 70 출력

print(c1.getN1()) # 결과 100 → c1 = Cal(100, 10)
