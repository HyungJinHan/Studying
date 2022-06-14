class Cal
  def initialize(n1, n2)
  # 초기화하는 기능의 코드
  # 생성자, constructor
    @n1 = n1
    @n2 = n2
    # @는 인스턴스의 변수를 의미
    # 생성된 인스턴스 내부에 모든 메소드에서 사용하도록 지정
  end

  def add() # 메소드
    return @n1 + @n2
    # 위에서 지정한 인스턴스 변수를 사용
  end

  def subtract()
    return @n1 - @n2
  end
end
# n1, n2로만 사용는 것은 지역변수
# @n1, @n2를 사용하는 것은 인스턴스 변수로 전역변수와 비슷

c1 = Cal.new(100, 10)
puts(c1.add()) # 더하기 / 결과 : 110
p c1.subtract() # 빼기 / 결과 : 90
# p "xxx" = puts("xxx")

c2 = Cal.new(50, 5)
puts(c2.add()) # 결과 : 55
p c2.subtract() # 결과 : 45
# p "xxx" = puts("xxx")
