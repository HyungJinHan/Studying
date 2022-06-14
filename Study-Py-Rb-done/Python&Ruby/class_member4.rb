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
end

class CalMultiply < Cal
  def multiply()
    result = @n1 * @n2
    @@_history.push("#{n1} * #{n2} = #{result}") # 배열의 끝에 인자 추가
    return result
  end
end

class CalDivide < CalMultiply
  def divide()
    result = @n1 / @n2
    @@_history.push("#{n1} / #{n2} = #{result}") # 배열의 끝에 인자 추가
    return result
  end
end

c1 = CalMultiply.new(100, 10) # 생성자도 상속받음
puts(c1.multiply()) # 결과 : 1000
puts(c1.add()) # 결과 : 110 (Cal에게 상속받음)
puts(c1.subtract()) # 결과 : 90 (Cal에게 상속받음)

c2 = CalDivide.new(200,10)
puts(c2.multiply()) # 결과 : 2000 (CalMultiply에게 상속받음)
puts(c2.divide()) # 결과 : 20

Cal.history()
# 결과
# 100 * 10 = 1000
# 100 + 10 = 110
# 100 - 10 = 90
# 200 * 10 = 2000
# 200 / 10 = 20

# 번외
a = "HSH"
b = "JHS"
c = "HHJ1"
d = "HHJ2"
fam = ["HSH", "JHS", "HHJ1", "HHJ2"]
fam_num = fam.length
puts("My family's member is #{a}, #{b}, #{c}, #{d} just 4")
# 결과 : My family's member is HSH, JHS, HHJ1, HHJ2 just 4
puts("My family's member is #{fam} just #{fam_num}")
# 결과 : My family's member is ["HSH", "JHS", "HHJ1", "HHJ2"] just 4
# 문자열 내부에 변수를 대치시키는 방법
