#!python
print("Content-type: text/html; charset=utf-8\n")
# ↑ Python을 연동시켜서 화면에 도출될 수 있게 하는 코드 ↑ (1~2)

class Cal(object):
    def __init__(self, n1, n2):
    # 초기화하는 기능의 코드
    # ()안에 임의의 값을 첫번째에 지정해야함
    # ()안의 임의의 첫번째 값은 해당 인스턴스를 의미
    # 다른 메소드에서도 사용할 수 있도록 하기 위함
        self.n1 = n1
        self.n2 = n2
        # 위의 인스턴스의 변수를 다른 메소드에서도 사용 가능

    def add(self): # 메소드
    # 인스턴스 변수 사용을 위해 ()에 self 입력
        return self.n1 + self.n2

    def subtract(self): # 메소드
        return self.n1 - self.n2

c1 = Cal(100, 10)
print(c1.add()) # 더하기 / 결과 : 110
print(c1.subtract()) # 빼기 / 결과 : 90

c2 = Cal(50, 5)
print(c2.add()) # 결과 : 55
print(c2.subtract()) # 결과 : 45
