#!python
print("Content-type: text/html; charset=utf-8\n")
# ↑ Python을 연동시켜서 화면에 도출될 수 있게 하는 코드 ↑ (1~2)

class Cs:
    count = 0
    # 메소드의 밖에서의 변수는 자동적으로 class 소속이 됨
    # 별도로 Cs. 이라는 class 소속을 지정할 필요 X
    def __init__(self): # 생성자
        Cs.count = Cs.count + 1
    # 인스턴스 생성을 생성자가 호출될 때,
    # class 소속의 count라는 변수가 1씩 더해짐
    @classmethod # or staticmethod
    def getCount(cls):
        return Cs.count
    # count라는 변수를 class의 소속으로 지정해서 모든 인스턴스가 사용할 수 있음

i1 = Cs()
i2 = Cs()
i3 = Cs()
i4 = Cs()
i5 = Cs()
i6 = Cs()

print(Cs.getCount()) # 결과 : 6
