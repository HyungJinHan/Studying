module CalMultiply
  def multiply()
    return @n1 * @n2
  end
end

module CalDivide
  def divide()
    return @n1 / @n2
  end
end

class Cal
  attr_accessor :n1, :n2
  include CalMultiply, CalDivide
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
  def setN2(n)
    if n.is_a?(Integer)
    # n이 정수인지를 체크하는 조건문
      @n2 = n
    end
  end
  def getN1()
    return @n1
  end
  def getN2()
    return @n2
  end
end

c = Cal.new(100, 10)
puts(c.add()) # 결과 : 110
puts(c.subtract()) # 결과 : 90
puts(c.multiply()) # 결과 : 1000 (module인 CalMultiply 가져옴)
puts(c.divide()) # 결과 : 10 (module인 CalDivide 가져옴)

c.setN1(500)
c.setN2(100)
print("n1 = ",c.getN1(),", ","n2 = ",c.getN2()) # 결과 : n1 =  500 , n2 = 100
print("\n")
puts(c.getN2()) # 결과 : 100
puts(c.multiply()) # 결과 : 50000 (module인 CalMultiply 가져옴)
puts(c.divide()) # 결과 : 5 (module인 CalDivide 가져옴)
