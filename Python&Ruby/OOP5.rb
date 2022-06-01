class C
  attr_reader :value
  # value라는 인스턴스 변수를 읽기 가능한 속성으로 지정
  attr_writer :value
  # value라는 인스턴스 변수를 쓰기 가능한 속성으로 지정
  attr_accessor :value # (attr_reader + attr_writer)
  # value라는 인스턴스 변수를 읽고 쓰기 가능한 속성으로 지정
  def initialize(n1)
  # 생성자
    @value = n1
  end
  def show()
    puts(@value)
  end
end

c1 = C.new(10)
puts(c1.value) # 결과 : 10
# attr_reader :value로 인해 외부에서 인스턴스 value 읽기 가능

c1.value = 100
puts(c1.value) # 결과 : 100
# attr_writer :value로 인해 외부에서 인스턴스 value 쓰기 가능
