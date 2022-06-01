#!python
print("Content-type: text/html; charset=utf-8\n")
# ↑ Python을 연동시켜서 화면에 도출될 수 있게 하는 코드 ↑ (1~2)

class Cal(object):
    _history = [] # _history의 내용을 배열로 지정
    def __init__(self, n1, n2):
    # 생성자, constructor
        if isinstance(n1, int):
            self.n1 = n1
        if isinstance(n2, int):
            self.n2 = n2
    def add(self): # 메소드
        result = self.n1 + self.n2
        Cal._history.append("%d + %d = %d" %(self.n1, self.n2, result)) # 배열의 끝에 인자 추가
        # 문자열("") 안에 지정하고 싶은 변수 입력 시 사용
        return result
    def subtract(self): # 메소드
        result = self.n1 - self.n2
        Cal._history.append("%d - %d = %d" %(self.n1, self.n2, result)) # 배열의 끝에 인자 추가
        # 문자열("") 안에 지정하고 싶은 변수 입력 시 사용
        return result
    def setN1(self, n):
        if isinstance(n, int):
        # 첫번째 인자가 두번째 인자의 인스턴스인지 체크하는 조건문
            self.n1 = n
    def getN1(self):
        return self.n1
    @classmethod
    def history(cls):
        for item in Cal._history:
            print(item)

class CalMultiply(Cal):
    def multiply(self):
        result = self.n1 * self.n2
        Cal._history.append("%d * %d = %d" %(self.n1, self.n2, result)) # 배열의 끝에 인자 추가
        # 문자열("") 안에 지정하고 싶은 변수 입력 시 사용
        return result

class CalDivide(CalMultiply):
    def divide(self):
        result = self.n1 / self.n2
        Cal._history.append("%d / %d = %d" %(self.n1, self.n2, result)) # 배열의 끝에 인자 추가
        # 문자열("") 안에 지정하고 싶은 변수 입력 시 사용
        return result

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

Cal.history()
# 결과
# 100 * 10 = 1000
# 100 + 10 = 110
# 100 - 10 = 90
# 200 * 10 = 2000
# 200 / 10 = 20
# 500 * 10 = 5000

# 번외
a = "HSH"
b = "JHS"
c = "HHJ1"
d = "HHJ2"
fam = ["HSH", "JHS", "HHJ1", "HHJ2"]
fam_num = len(fam)
print("My family's member is %s, %s, %s, %s just 4" %(a, b, c, d))
# 결과 : My family's member is HSH, JHS, HHJ1, HHJ2 just 4
print("My family's member is %s just %d" %(fam, fam_num))
# 결과 : My family's member is ['HSH', 'JHS', 'HHJ1', 'HHJ2'] just 4
# 문자열 내부에 변수를 대치시키는 방법
# %s : "hhj"와 같은 문자열
# %d : 1, 2와 같은 정수
# %f : 3.14와 같은 실수
