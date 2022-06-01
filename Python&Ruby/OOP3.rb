class C
  def initialize(n1)
  # 생성자
    @value = n1
  end
  def show()
    puts(@value)
  end
  def getValue()
    return @value
  end
  def setValue(n1)
  # value값 지정을 위해 ()에 n1 입력
    @value = n1
  end
end

c1 = C.new(10)
puts(c1.getValue()) # 결과 : 10
# return @value으로 인해 C.new(10)으로 정한 값인 10 출력

c1.setValue(100)
puts(c1.getValue()) # 결과 : 100
# c1.setValue(100)을 통해 100을 value값으로 지정 후 출력

c1.value = 1000 # 결과 : Error
puts(c1.value) # 결과 : Error
# 외부에서 인스턴스 내부의 메소드에 접근 불가
