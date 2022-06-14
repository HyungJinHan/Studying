class Cal
  def initialize(n1, n2)
  # 생성자, constructor
    @n1 = n1
    @n2 = n2
  end
  def add() # 메소드
    return @n1 + @n2
  end
  def subtract()
    return @n1 - @n2
  end
  def setN1(n)
    if n.is_a?(Integer)
    # n이 정수인지를 체크하는 조건문
      @n1 = n
    end
  end
  def getN1()
    return @n1
  end
end

c1 = Cal.new(100, 10)
puts(c1.add()) # 더하기 / 결과 : 110
p c1.subtract() # 빼기 / 결과 : 90
# p "xxx" = puts("xxx")

c1.setN1("one")
puts(c1.add())
# 위의 문자인 1은 무시되고 기존의
# c1 = Cal.new(100, 10) 값을 더한 값인 110 출력

c1.setN1(1000)
puts(c1.add()) # 더하기 / 결과 : 1010

puts(c1.getN1()) # 결과 1000 → c1.setN1(1000)
