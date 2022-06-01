class Cs
  @@count = 0
  # count라는 변수의 값을 최초로 0으로 설정
  def initialize() # 생성자
    @@count = @@count + 1
    # @ : 인스턴스 소속의 변수 / @@ : class 소속의 변수
  end
  # 인스턴스 생성을 생성자가 호출될 때,
  # class 소속의 count라는 변수가 1씩 더해짐
  def Cs.getCount()
    return @@count
  end
end
# count라는 변수를 class의 소속으로 지정해서 모든 인스턴스가 사용할 수 있음

i1 = Cs.new()
i2 = Cs.new()
i3 = Cs.new()
i4 = Cs.new()
i5 = Cs.new()
i6 = Cs.new()

puts(Cs.getCount()) # 결과 : 6
