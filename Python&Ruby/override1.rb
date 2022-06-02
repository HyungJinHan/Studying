class Cal
  attr_accessor :n1, :n2
  @@_history = [] # _history의 내용을 배열로 지정
  def initialize(n1, n2)
  # 생성자, constructor
    @n1 = n1
    @n2 = n2
  end
  def add() # 메소드
    result = @n1 + @n2
    @@_history.push("#{n1} + #{n2} = #{result}") # 배열의 끝에 인자 추가
    # #{} : {}안에 들어가 있는 내용을 변수로 취급
    return result
  end
  def subtract()
    result = @n1 - @n2
    @@_history.push("#{n1} - #{n2} = #{result}") # 배열의 끝에 인자 추가
    return result
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
  def Cal.history()
    for item in @@_history
    # for in문을 통해 @@_history라는 변수의 내용을 하나씩 출력
      puts(item)
    end
  end
  def info()
    return "Cal → n1 : #{@n1}, n2 : #{@n2}"
  end
end

class CalMultiply < Cal
  def multiply()
    result = @n1 * @n2
    @@_history.push("#{n1} * #{n2} = #{result}") # 배열의 끝에 인자 추가
    return result
  end
  def info()
    return "CalMultiply → #{super()}"
    # 부모 class의 값을 추가
  end
end

class CalDivide < CalMultiply
  def divide()
    result = @n1 / @n2
    @@_history.push("#{n1} / #{n2} = #{result}") # 배열의 끝에 인자 추가
    return result
  end
  def info()
    return "CalDivide → #{super()}"
    # 부모 class의 값을 추가
  end
end

c0 = Cal.new(500,50)
puts(c0.info())
# 결과 : Cal → n1 : 500, n2 : 50

c1 = CalMultiply.new(100, 10) # 생성자도 상속받음
puts(c1.info())
# 결과 : CalMultiply → Cal → n1 : 100, n2 : 10
puts(c1.multiply()) # 결과 : 1000
puts(c1.add()) # 결과 : 110 (Cal에게 상속받음)
puts(c1.subtract()) # 결과 : 90 (Cal에게 상속받음)

c2 = CalDivide.new(200,10)
puts(c2.info())
# 결과 : CalDivide → CalMultiply → Cal → n1 : 200, n2 : 10
puts(c2.multiply()) # 결과 : 2000 (CalMultiply에게 상속받음)
puts(c2.divide()) # 결과 : 20

c1.setN1(500)
puts(c1.info())
# 결과 : CalMultiply → Cal → n1 : 500, n2 : 10
puts(c1.getN1()) # 결과 500
puts(c2.getN1()) # 결과 : 200
puts(c1.multiply()) # 결과 : 5000

Cal.history()
# 결과
# 100 * 10 = 1000
# 100 + 10 = 110
# 100 - 10 = 90
# 200 * 10 = 2000
# 200 / 10 = 20
