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

class CalMultiply < Cal
  def multiply()
    return @n1 * @n2
  end
end

class CalDivide < CalMultiply
  def divide()
    return @n1 / @n2
  end
end

c1 = CalMultiply.new(100, 10) # 생성자도 상속받음
puts(c1.multiply()) # 결과 : 1000
puts(c1.add()) # 결과 : 110 (Cal에게 상속받음)
puts(c1.subtract()) # 결과 : 90 (Cal에게 상속받음)

c2 = CalDivide.new(200,10)
puts(c2.multiply()) # 결과 : 2000 (CalMultiply에게 상속받음)
puts(c2.divide()) # 결과 : 20

c1.setN1(500)
p c1.getN1 # 결과 : 500
p c2.getN1 # 결과 : 200
p c1.multiply # 결과 : 5000
# p xxx = puts()
